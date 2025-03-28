# 스택

def solution(prices):
    n = len(prices)
    answer = [i for i in range(n - 1, -1, -1)]
    stack = []

    for j in range(n):

        while stack:
            if stack[-1][0] > prices[j]:
                price, idx = stack.pop()
                answer[idx] = j - idx

            else:
                break

        stack.append((prices[j], j))

    return answer