'''
- 현재 꽃을 선택하는 경우 / 선택하지 않는 경우
- 현재 꽃의 바로 이전 꽃 아름다움 값
'''

def cal_beauty(a, b):
    return (abs(a - b))**2

N = int(input())
flowers = [0] + list(map(int, input().split()))
dp = [0] * (N+1)
answer = 0

for i in range(1, N+1):
    for j in range(1, i):

        cur_beauty = cal_beauty(flowers[i], flowers[j])
        dp[i] = max(dp[i], dp[j] + cur_beauty)
        answer = max(answer, dp[i])

print(answer)