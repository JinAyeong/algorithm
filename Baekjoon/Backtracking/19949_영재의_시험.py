import sys
input = sys.stdin.readline

answers = list(map(int, input().split()))
omr = []
result = 0

def dfs(i, cnt):
    global result

    if i == 10:
        if cnt >= 5:
            result += 1
        return

    for j in range(1, 6):
        if i >= 2 and omr[i - 1] == omr[i - 2] == j:
            continue

        omr.append(j)
        dfs(i + 1, cnt + (1 if j == answers[i] else 0))
        omr.pop()

dfs(0, 0)
print(result)
