def solution(n, s):
    if n > s:
        return [-1]

    base_num = s // n
    answer = [base_num for _ in range(n)]
    last_num = s - base_num * n

    for i in range(n - 1, n - last_num - 1, -1):
        answer[i] += 1

    return answer