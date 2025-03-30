def dfs(i, num):
    global lotto

    if i == 6:
        print(*lotto)
        return

    for j in range(num+1, k):
        lotto.append(S[j])
        dfs(i+1, j)
        lotto.pop()

while True:
    k, *S = list(map(int, input().split()))
    if k == 0:
        break

    lotto = []

    for i in range(k):
        lotto.append(S[i])
        dfs(1, i)
        lotto.pop()

    print()
