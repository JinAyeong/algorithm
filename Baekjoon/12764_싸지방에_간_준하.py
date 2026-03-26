'''
싸지방에 들어왔을때 번호가 가장 작은 자리에 앉기
모든 사람이 기다리지 않고 싸지방을 이용할 수 있는 컴퓨터의 최소 개수
'''

from heapq import heappop, heappush

N = int(input())
waiting = sorted(tuple(map(int, input().split())) for _ in range(N))
using = []   # (끝나는 시간, 자리 번호)
empty = []   # 사용 가능한 자리 번호
used_cnt = []

for P, Q in waiting:
    
    # 끝난 자리 반환
    while using and using[0][0] <= P:
        _, idx = heappop(using)
        heappush(empty, idx)
    
    # 사용할 자리 결정
    if empty:
        idx = heappop(empty)
    else:
        idx = len(used_cnt)
        used_cnt.append(0)
    
    # 사용 처리
    used_cnt[idx] += 1
    heappush(using, (Q, idx))

print(len(used_cnt))
print(*used_cnt)