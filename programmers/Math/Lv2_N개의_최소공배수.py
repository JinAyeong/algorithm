# math 구현
def solution(arr):

    # 최대공약수
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    # 최소공배수
    def lcm(a, b):
        return a * b // gcd(a, b)

    answer = arr[0]

    for num in arr[1:]:
        answer = lcm(answer, num)

    return answer


# 브루트포스
def solution(arr):
    answer = arr[-1]
    N = len(arr)
    found = False

    while not found:

        for i in range(N - 1, -1, -1):
            if answer % arr[i] != 0:
                answer += 1
                break

            if i == 0:
                found = True

    return answer