N = int(input())
numbers = list(map(int, input().split()))
used = [False] * N
result = 0

def dfs(i, lst, cur):
    global result

    if i == N:
        result = max(result, cur)
        return

    for j in range(N):
        if not used[j]:
            used[j] = True
            lst.append(numbers[j])
            if i > 0:
                dfs(i + 1, lst, cur + abs(lst[-1] - lst[-2]))
            else:
                dfs(i + 1, lst, 0)
            lst.pop()
            used[j] = False

dfs(0, [], 0)
print(result)
