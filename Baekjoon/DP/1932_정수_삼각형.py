n = int(input())
dp = [0] * n

for i in range(n):
    arr = list(map(int, input().split()))
    new_dp = [0] * n
    if i == 0:
        new_dp[0] = arr[0]

    else:
        for j in range(i+1):
            left = (dp[j-1] if j != 0 else 0)
            right = (dp[j] if j != i else 0)
            new_dp[j] = max(left + arr[j], right + arr[j])
    dp = new_dp

print(max(dp))