#!/usr/bin/env python3
"""개인 레포(algorithm) 풀이를 스터디 레포(AlgoStudy)로 동기화하는 도구.

처리 흐름:
    1. AlgoStudy 내 개인 폴더(yyong) 기준 최근 풀이일 자동 파악
    2. 해당 시점 이후 algorithm 에만 존재하는 미반영 문제 선별 (이름 기준)
    3. yyong/YYYY.MM/YYMMDD_문제이름.ext 형태로 풀이 복제
    4. '[플랫폼] 문제이름 / 난이도' 컨벤션 + 실제 풀이일 커밋 일자로 커밋 생성

원격 반영(push) 미수행. 검토 후 사용자 직접 push/PR 전제.

사용 예:
    python3 algostudy_sync.py            # 실제 동기화
    python3 algostudy_sync.py --dry-run  # 반영 예정 내역 미리보기
    python3 algostudy_sync.py --since 2025-06-01   # 기준일 직접 지정
"""
import os, re, sys, subprocess, shutil, collections

# Windows 콘솔 기본 코드페이지(cp949)에서 한글 출력이 깨지는 것 방지
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

# ── 설정값 ─────────────────────────────────────────────
# 스크립트 위치 디렉터리를 algorithm 레포로 간주, 인접 AlgoStudy 레포 존재 전제
ALGO = os.path.dirname(os.path.abspath(__file__))
STUDY = os.path.join(os.path.dirname(ALGO), "AlgoStudy")
STUDY_BRANCH = "ayeong"        # AlgoStudy 커밋 대상 개인 작업 브랜치
USER_DIR = "yyong"             # 개인 폴더. 타인 폴더는 대상에서 제외
SRC_DIRS = ("Baekjoon/", "programmers/", "NeetCode/")
EXTS = (".py", ".sql", ".js")
TAG_BY_DIR = {"Baekjoon/": "BOJ", "programmers/": "PGS", "NeetCode/": "NTC"}

# 커밋 메시지 내 난이도 표기 식별용 패턴
DIFF_RE = re.compile(
    r'(실버|골드|브론즈|플래티넘|플래티|다이아몬드|다이아|루비|'
    r'Lv\s*\d+|Level\s*\d+|Easy|Medium|Hard)\s*\d*', re.I)

DRY = "--dry-run" in sys.argv


def git(args, cwd, **kw):
    # 한글 경로 이스케이프 방지 위한 quotepath 비활성화 실행
    # encoding 미지정 시 Windows 로케일(cp949)로 디코딩을 시도해 UTF-8 커밋 메시지에서 깨짐 발생
    return subprocess.run(["git", "-c", "core.quotepath=false", *args],
                          cwd=cwd, capture_output=True, text=True,
                          encoding="utf-8", **kw)


def normalize(stem):
    # 문제 동일성 비교용 정규화. 번호/난이도 접두·구분 기호 제거 후 순수 이름만 유지
    core = re.sub(r'^(\d+|Lv\d+)_', '', stem)
    return re.sub(r'[^0-9a-z가-힣]', '', core.lower())


def name_core(stem):
    # 파일명 생성용 이름. 밑줄 보존
    return re.sub(r'^(\d+|Lv\d+)_', '', stem)


def tag_for(path):
    # 경로 소속 플랫폼의 태그 반환
    for d, t in TAG_BY_DIR.items():
        if path.startswith(d):
            return t
    return None


# ── AlgoStudy 현재 상태 파악 ───────────────────────────
def study_state():
    """기등록 문제 이름 집합 + 파일명 기반 최근 풀이일 반환."""
    names, max_date = set(), None
    base = os.path.join(STUDY, USER_DIR)
    for root, _, files in os.walk(base):
        for f in files:
            if f.startswith('.'):
                continue
            stem = os.path.splitext(f)[0]
            names.add(normalize(stem))
            # YYMMDD_ 형식 파일명에 한해 날짜 신뢰
            m = re.match(r'^(\d{6})_', stem)
            if m:
                d = m.group(1)
                if max_date is None or d > max_date:
                    max_date = d
    since = None
    if max_date:
        since = f"20{max_date[:2]}-{max_date[2:4]}-{max_date[4:6]}"
    return names, since


# ── algorithm 문제 메타데이터 수집 ─────────────────────
def algo_problems():
    """문제별 최초 풀이일·관련 커밋 메시지·현재 대표 경로 수집.

    다수의 레포 재구성 이력 고려, 재배치 왜곡 방지 위한 이력 전체 최솟값 채택.
    """
    out = git(["log", "--name-only", "--date=short",
               "--pretty=format:@@%ad|%s"], ALGO).stdout
    earliest, subjects = {}, collections.defaultdict(list)
    cur_date = cur_subj = None
    for line in out.splitlines():
        if line.startswith("@@"):
            cur_date, cur_subj = line[2:].split("|", 1)
        elif line.strip():
            p = line.strip()
            if not p.startswith(SRC_DIRS) or not p.endswith(EXTS):
                continue
            n = normalize(os.path.splitext(os.path.basename(p))[0])
            if n not in earliest or cur_date < earliest[n]:
                earliest[n] = cur_date
            subjects[n].append(cur_subj)

    # 동일 문제 다중 경로 가능성 고려, 분류 폴더 정리 경로를 대표로 채택
    cur_files = git(["ls-files", *[d.rstrip("/") for d in SRC_DIRS]], ALGO).stdout.splitlines()
    canonical = {}
    for p in cur_files:
        if not p.endswith(EXTS):
            continue
        stem = os.path.splitext(os.path.basename(p))[0]
        n = normalize(stem)
        has_num = bool(re.match(r'^(\d+|Lv\d+)_', stem))
        score = p.count("/") * 10 + (5 if has_num else 0)
        if n not in canonical or score > canonical[n][0]:
            canonical[n] = (score, p, stem)
    return earliest, subjects, canonical


def extract_diff(subjs):
    # 메시지 말미 '/ 난이도' 형태 우선 탐색, 부재 시 본문 패턴 탐색
    for s in subjs:
        m = re.search(r'/\s*([^/]+?)\s*$', s)
        if m and DIFF_RE.search(m.group(1)):
            return m.group(1).strip()
    for s in subjs:
        m = DIFF_RE.search(s)
        if m:
            return m.group(0).strip()
    return None


def main():
    if not os.path.isdir(STUDY):
        print(f"AlgoStudy 레포 탐색 실패: {STUDY}")
        return

    # 의도치 않은 브랜치로의 커밋 누적 방지
    cur = git(["rev-parse", "--abbrev-ref", "HEAD"], STUDY).stdout.strip()
    if cur != STUDY_BRANCH:
        print(f"AlgoStudy 현재 브랜치 '{cur}'. '{STUDY_BRANCH}' 전환 후 재시도 필요.")
        print(f"  (cd {STUDY} && git checkout {STUDY_BRANCH})")
        return
    if git(["status", "--porcelain"], STUDY).stdout.strip():
        print("AlgoStudy 미커밋 변경 존재. 정리 후 재시도 필요.")
        return

    have, auto_since = study_state()
    since = auto_since
    for i, a in enumerate(sys.argv):
        if a == "--since" and i + 1 < len(sys.argv):
            since = sys.argv[i + 1]
    print(f"기준일(해당 일자 이후 풀이분 대상): {since or '(제한 없음)'}")

    earliest, subjects, canonical = algo_problems()
    rows = []
    for n, (score, path, stem) in canonical.items():
        # 기등록·날짜 미상·기준일 이전 항목 제외
        if n in have:
            continue
        date = earliest.get(n)
        if not date:
            continue
        if since and date < since:
            continue
        rows.append((date, path, stem, tag_for(path), extract_diff(subjects.get(n, []))))
    rows.sort()

    if not rows:
        print("반영 대상 없음. (이미 최신 상태)")
        return
    print(f"반영 대상: {len(rows)}개\n")

    made = 0
    for date, path, stem, tag, diff in rows:
        if not tag:
            continue
        yymmdd = date.replace("-", "")[2:]
        ym = date[:7].replace("-", ".")
        core = name_core(stem)
        ext = os.path.splitext(path)[1]
        rel = os.path.join(USER_DIR, ym, f"{yymmdd}_{core}{ext}")
        tgt = os.path.join(STUDY, rel)
        msg = f"[{tag}] {core.replace('_', ' ')}" + (f" / {diff}" if diff else "")
        # 난이도 미확인 시 후속 보완용 표시만 유지
        warn = "" if diff else "   (난이도 미확인)"

        if os.path.exists(tgt):
            print(f"= 기존재로 건너뜀: {rel}")
            continue
        if DRY:
            print(f"(dry-run) {rel}")
            print(f"          {msg}{warn}")
            continue

        os.makedirs(os.path.dirname(tgt), exist_ok=True)
        shutil.copyfile(os.path.join(ALGO, path), tgt)
        git(["add", "--", rel], STUDY)
        # 커밋 일자를 실제 풀이일에 일치
        env = dict(os.environ)
        env["GIT_AUTHOR_DATE"] = env["GIT_COMMITTER_DATE"] = date + "T12:00:00"
        r = subprocess.run(["git", "commit", "-m", msg, "--", rel],
                           cwd=STUDY, env=env, capture_output=True, text=True,
                           encoding="utf-8")
        if r.returncode == 0:
            made += 1
            print(f"반영: {rel}  ->  {msg}{warn}")
        else:
            print(f"커밋 실패: {rel}: {r.stderr.strip()}")

    if DRY:
        print(f"\n(dry-run) 반영 예정 {len(rows)}개. 실제 반영 시 --dry-run 미지정 실행.")
    else:
        print(f"\n완료: {made}개 커밋 생성 (push 미수행).")
        print(f"검토 후: cd {STUDY} && git log --oneline && git push origin {STUDY_BRANCH}")


if __name__ == "__main__":
    main()
