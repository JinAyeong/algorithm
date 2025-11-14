'''
최소 길이 사이클 조건
- 출발지점을 제외한 다른 방문노드 -> 방문 안함
- 플로이드 워셜 구현
'''
V, E = map(int, input().split())
adjl = [[] for _ in range(V+1)]
dist = [[float('inf')] * (V+1) for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c)

result = float('inf')

for i in range(1, V+1):
    for j in range(1, V+1):
        for k in range(1, V+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

result = min(dist[n][n] for n in range(1, V+1))
print(result if result != float('inf') else -1)


######################################################################
# 다익스트라 -> 시간초과 : V만큼 다익스트라 실행

# from heapq import heappop, heappush
# import sys
# input = sys.stdin.readline

# V, E = map(int, input().split())
# adjl = [[] for _ in range(V+1)]

# for _ in range(E):
#     a, b, c = map(int, input().split())
#     adjl[a].append((b, c))

# result = float('inf')

# for start in range(1, V+1):

#     dist = [float('inf')] * (V+1)
#     dist[start] = 0
#     heap = [(0, start)]
#     while heap:
        
#         cur_d, cur_n = heappop(heap)

#         if dist[cur_n] < cur_d:
#             continue

#         for next_n, w in adjl[cur_n]:
#             next_d = w + cur_d
#             if next_n == start:
#                 result = min(result, next_d)

#             if dist[next_n] > next_d:
#                 dist[next_n] = next_d
#                 heappush(heap, (next_d, next_n))

# if result == float('inf'):
#     print(-1)
# else:
#     print(result)