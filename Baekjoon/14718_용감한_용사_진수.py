'''
이기는 조건
1. 적의 힘 <= 진수의 힘
2. 적의 민첩 <= 진수의 민첩
3. 적의 지능 <= 진수의 지능
최소 k명의 병사를 이길 수 있게 하는 최소 스탯 포인트
'''

N, K = map(int, input().split())
stats = [list(map(int, input().split())) for _ in range(N)]

