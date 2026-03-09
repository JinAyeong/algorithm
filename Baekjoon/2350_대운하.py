'''
N개의 도시, M개의 운하
배의  폭 <= 운하의 폭
K개의 노선
'''

N, M, K = map(int, input().split())
canals = []
graph = [tuple(map(int, input().split())) for _ in range(N)]

for _ in range(M):
    i, j, w = map(int, input().split())
    