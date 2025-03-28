n = int(input())
m = int(input())
adjl = [[] for _ in range(n+1)]
invited = [False] * (n+1)
invited[1] = True

for _ in range(m):
    a, b = map(int, input().split())
    adjl[a].append(b)
    adjl[b].append(a)

for i in adjl[1]:
    invited[i] = True
    for j in adjl[i]:
        invited[j] = True

print(invited.count(True) - 1)