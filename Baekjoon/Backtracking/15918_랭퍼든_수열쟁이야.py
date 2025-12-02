'''
랭퍼든 수열 : 1이상 n이하의 자연수가 두개씩 들어있다. 두개의 n 사이에 정확히 n개의 수가 있다
조건 추가 : x번째 수와 y번째 수는 같다

used가 0이면 숫자 하나 추가, 적절한 위치에 또 하나 추가
'''

n, x, y = map(int, input().split())
used = [False] * (n+1)
perm = [0] * (2 * n + 1)
answer = 0

k = abs(x-y)-1

if k < 1 or k > n:
    print(0)
    exit()

perm[x] = perm[y] = k
used[k] = True

def dfs(i):
    global answer

    if i == 2*n+1:
        answer += 1
        return
    
    if perm[i] != 0:
        dfs(i+1)
        return
    
    for j in range(1, n+1):
        if not used[j] and i+j+1 <= 2*n and perm[i+j+1] == 0:
            used[j] = True
            perm[i] = perm[i+j+1] = j
            dfs(i+1)
            used[j] = False
            perm[i] = perm[i+j+1] = 0

dfs(1)

print(answer)