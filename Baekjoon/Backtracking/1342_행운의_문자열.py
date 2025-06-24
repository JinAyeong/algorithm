S = input()
N = len(S)
used = [False] * N
new_S = []
answer = 0

def dfs(i):
    global answer

    if i == N:
        answer += 1
        return

    cur_S = set()

    for j in range(N):
        if used[j]:
            continue

        if new_S and new_S[-1] == S[j]:
            continue

        if S[j] in cur_S:
            continue

        cur_S.add(S[j])
        used[j] = True
        new_S.append(S[j])
        dfs(i+1)
        new_S.pop()
        used[j] = False

dfs(0)

print(answer)