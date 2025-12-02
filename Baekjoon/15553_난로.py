'''
i번째 친구 : 구사과의 방에 Ti도착 -> Ti+1에 나감
성냥 총 K번 켤 수 있음
'''

N, K = map(int, input().split())
visit_time = [int(input()) for _ in range(N)]

