def solution(n, k):
    answer = []
    numbers = list(range(1, n + 1))
    k -= 1

    for i in range(n, 0, -1):
        factorial = 1

        for j in range(1, i):
            factorial *= j

        idx = k // factorial
        answer.append(numbers.pop(idx))

        k %= factorial

    return answer