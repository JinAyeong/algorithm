'''
S (끝내야하는 시간) 기준으로 정렬
현재 가장 늦게 일어나도 되는 시간, 지금 보는 일의 끝내야하는 시간 중 min + T 갱신
'''
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x:-x[1])

cur_time = float('inf')

for t, s in arr:
    cur_time = min(cur_time, s) - t

print(cur_time if cur_time >=0 else -1)