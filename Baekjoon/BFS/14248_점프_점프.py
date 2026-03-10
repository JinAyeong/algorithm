'''
돌다리의 숫자만큼 왼쪽 또는 오른쪽으로 점프 가능
'''
from collections import deque

n = int(input())
arr = list(map(int, input().split()))
s = int(input()) - 1

answer = 1
q = deque([s])
visited = [False] * n
visited[s] = True

while q:
    cur = q.popleft()

    for next in [cur + arr[cur], cur - arr[cur]]:
        if 0 <= next < n and not visited[next]:
            q.append(next)
            visited[next] = True
            answer += 1

print(answer)