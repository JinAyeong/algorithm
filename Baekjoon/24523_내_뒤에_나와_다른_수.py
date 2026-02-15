'''
내 뒤에 있는 수 중, 나와 다른 수이고, 가장 장은 수의 인덱스 +1 출력
'''

import sys
input = sys.stdin.readline

N = int(input())
perms = list(map(int, input().split()))
min_arr = [float('inf')] * N
