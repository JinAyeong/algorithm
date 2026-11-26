'''
5 60
30 10 20 35 40
3 0 3 5 4

메모리 합이 60이상이되는 최소 비용
Mi를 선택 / 미선택
'''

N, M = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))

