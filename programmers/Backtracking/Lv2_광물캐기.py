from itertools import permutations

# 한번 선택한 곡괭이는 5번 사용
# 광물은 순서대로만 캘 수 있음
# 모든 광물을 캐거나, 곡괭이가 없을 때 까지 사용

def picking(d, i, s, m, total_p, minerals):  # 남은 곡괭이 수(d, i, s), 현재 광물 번호(m), 지금까지 피로도(total_p)

    global answer, p

    if (d == 0 and i == 0 and s == 0) or m == len(minerals):
        answer = min(total_p, answer)
        return

    if total_p > answer:
        return

    # 다이아몬드 사용
    if d > 0:
        cur_p = 0 # 지금 선택한 곡괭이 쓸 때의 피로도
        cnt = 0   # 지금 선택한 곡괭이 사용 횟수

        for c in range(5):
            if m + c == len(minerals):  # 광물 다 캤으면 break
                break
            cur_p += p['diamond'][minerals[m + c]]   # 현재 인덱스 광물 캘 때의 피로도
            cnt += 1   # 사용 횟수 추가

        # 다음 곡괭이 선택
        picking(d - 1, i, s, m + cnt, total_p + cur_p, minerals)

    # 철 사용
    if i > 0:
        cur_p = 0
        cnt = 0

        for c in range(5):
            if m + c == len(minerals):
                break
            cur_p += p['iron'][minerals[m + c]]
            cnt += 1

        picking(d, i - 1, s, m + cnt, total_p + cur_p, minerals)

    # 돌 사용
    if s > 0:
        cur_p = 0
        cnt = 0

        for c in range(5):
            if m + c == len(minerals):
                break
            cur_p += p['stone'][minerals[m + c]]
            cnt += 1

        picking(d, i, s - 1, m + cnt, total_p + cur_p, minerals)


def solution(picks, minerals):  # 곡괭이 수, 광물 리스트
    global answer, p

    answer = float('inf')  # 최소 피로도

    p = {
        'diamond': {'diamond': 1, 'iron': 1, 'stone': 1},
        'iron': {'diamond': 5, 'iron': 1, 'stone': 1},
        'stone': {'diamond': 25, 'iron': 5, 'stone': 1},
    }

    picking(picks[0], picks[1], picks[2], 0, 0, minerals)

    return answer