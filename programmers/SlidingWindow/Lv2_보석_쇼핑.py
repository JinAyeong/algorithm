from collections import defaultdict


def solution(gems):
    total = len(set(gems))  # 보석 종류의 총 개수
    left = 0
    result = [0, len(gems)]
    select = defaultdict(int)

    # 끝 점을 순회하며 최솟값 찾기
    for right in range(len(gems)):
        select[gems[right]] += 1  # 보석 추가

        # 조건이 맞으면
        while len(select) == total:

            # 현재 구간이 기존 최솟값이라면 갱신
            if right - left < result[1] - result[0]:
                result = [left + 1, right + 1]

            # 구간 축소하며 최솟값 찾기
            select[gems[left]] -= 1
            if select[gems[left]] == 0:
                del select[gems[left]]

            left += 1

    return result