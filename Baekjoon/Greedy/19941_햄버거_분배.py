N, K = map(int, input().split())
table = list(input())
result = 0

for i in range(N):

    if table[i] == 'P':
        for j in range(i-K, i+K+1):
            if 0 <= j < N and table[j] == 'H':
                table[j] = 'X'
                result += 1
                break

print(result)