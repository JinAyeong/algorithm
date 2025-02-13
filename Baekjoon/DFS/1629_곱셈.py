A, B, C = map(int, input().split())

def dfs(num):
    if num == 0:
        return 1

    if num == 1:
        return A % C

    half = dfs(num // 2)
    origin = half * half % C

    if num % 2 == 1:
        origin = origin * A % C

    return origin

print(dfs(B))