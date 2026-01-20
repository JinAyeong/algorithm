import sys
input = sys.stdin.readline

N = int(input())
village = [list(map(int, input().split())) for _ in range(N)]

def distance(A, B):
    return abs(A[0] - B[0]) + abs(A[1] - B[1]) + abs(A[2] - B[2])

result = float('inf')

for i in range(N):

    m1 = float('inf')
    m2 = float('inf')

    for j in range(N):
        if i == j:
            continue

        d = distance(village[i], village[j])

        if d < m1:
            m2 = m1
            m1 = d
        elif d < m2:
            m2 = d

    result = min(result, m1 + m2)

print(result)
