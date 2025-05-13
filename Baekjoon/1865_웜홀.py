'''
N개의 지점 사이에 M개의 도로와 W개의 웜홀

'''

for _ in range(int(input())):

    N, M, W = map(int, input().split())
    adjl = [[] for _ in range(N+1)]

    for _ in range(M):
        # 시작지점, 도착지점, 줄어드는 시간
        S, E, T = map(int, input().split())
        adjl[S].append((E, T))
        adjl[E].append((S, T))

    def wormhole(n):

