# 스위치 눌러야하는 수
# i번 스위치 : i의 배수 번호를 가지는 전구 모두 반전

import sys
sys.setrecursionlimit(10**6)

bulbs = list(input())
N = len(bulbs)
result = -1

def switch(i, arr):

    for j in range(i, N, i+1):
        arr[j] = ('Y' if arr[j] == 'N' else 'N')

    return arr

def dfs(n, arr):
    global result

    if all(i == 'N' for i in arr):
        result = n
        return

    for j in range(N):
        if arr[j] == 'Y':
            new_arr = switch(j, arr)
            dfs(n+1, new_arr)

dfs(0, bulbs)

print(result)