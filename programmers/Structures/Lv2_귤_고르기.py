def solution(k, tangerine):
    answer = 0
    cnt = {}

    for t in tangerine:
        if t in cnt:
            cnt[t] += 1
        else:
            cnt[t] = 1

    sorted_cnt = list(cnt.items())
    sorted_cnt.sort(key=lambda x: -x[1])

    for key, value in sorted_cnt:
        k -= value
        answer += 1
        if k <= 0:
            break

    return answer