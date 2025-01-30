#------------------------------------------
# 슬라이딩 윈도우

N, X = map(int, input().split())
visit = list(map(int, input().split()))

cur_visit = sum(visit[:X])
result = 0
cnt = 0

for i in range(X-1,N):
    if i != X-1:
        cur_visit -= visit[i-X]
        cur_visit += visit[i]

    if cur_visit > result:
        result = cur_visit
        cnt = 1

    elif cur_visit == result:
        cnt += 1

if result == 0:
    print('SAD')

else:
    print(result)
    print(cnt)