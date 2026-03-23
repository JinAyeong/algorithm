N, M = map(int, input().split())
mp = [input() for _ in range(N)]

def solve(i, j):

    white = black = 0

    for a in range(i, i+8):
        for b in range(j, j+8):
            if (a%2 == 0 and b%2 == 0) or (a%2 == 1 and b%2 == 1):
                if mp[a][b] == 'B':
                    white += 1
                else:
                    black += 1
            
            elif (a%2 == 1 and b%2 == 0) or (a%2 == 0 and b%2 == 1):
                if mp[a][b] == 'W':
                    white += 1
                else:
                    black += 1

    return min(white, black)

answer = float('inf')

for i in range(N-7):
    for j in range(M-7):
        answer = min(answer, solve(i, j))

print(answer)