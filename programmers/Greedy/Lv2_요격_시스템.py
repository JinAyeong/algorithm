from heapq import heappop, heapify

def solution(targets):
    answer = 1

    heapify(targets)

    cur_s, cur_e = heappop(targets)

    while targets:

        s, e = heappop(targets)

        if s < cur_e:
            cur_e = min(cur_e, e)
        else:
            answer += 1
            cur_s, cur_e = s, e

    return answer