'''
i번 스위치 클릭 -> i-1, i, i+1 스위치 변경
스위치 최소 클릭 수
'''
from copy import deepcopy

N = int(input())
bulb = list(input().strip())
target_bulb = list(input().strip())
switch_bulb = {'1':'0', '0':'1'}

def solve(arr, is_press_first_switch):
    cnt = 0

    if is_press_first_switch:
        cnt += 1
        for switch in [0, 1]:
            if 0 <= switch < N:
                arr[switch] = switch_bulb[arr[switch]]

    for i in range(1, N):

        if arr[i-1] != target_bulb[i-1]:
            cnt += 1
            for switch in [i-1, i, i+1]:
                if 0 <= switch < N:
                    arr[switch] = switch_bulb[arr[switch]]

    if arr == target_bulb:
        return cnt
    
    return float('inf')

ans = min(solve(deepcopy(bulb), True), solve(deepcopy(bulb), False))

print(ans if ans != float('inf') else -1)