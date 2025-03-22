dp = [0] * 1000001

dp[1] = 1
n = int(input())
cur = dp[1]
i = 1

while cur < n:
    i += 1
    dp[i] = 1 + dp[i - dp[dp[i - 1]]]
    cur += dp[i]

# print(dp[:i+1])
print(i)

#------------------------------------------------------
# N = int(input())
#
# if N == 1:
#     print(1)
#     exit(0)
#
# # 골롱 수열의 첫 번째와 두 번째 값 초기화
# # golomb[i]는 i번째 골롱 수열의 값
# # 첫 번째 값은 1, 두 번째 값은 2
#
# golomb = [1, 2]
# last_val = 2  # 현재 골롱 수열에서 마지막으로 추가된 숫자의 위치
# idx = 2  # 현재 채워야 하는 숫자
#
# while last_val < N:
#     count = golomb[idx - 1]  # 현재 숫자가 골롱 수열에서 몇 번 등장해야 하는지 확인
#     for _ in range(count):  # 해당 숫자를 count 횟수만큼 추가
#         golomb.append(idx)  # 현재 숫자를 골롱 수열에 추가
#         last_val += 1  # 마지막 위치 증가
#         if last_val == N:  # 원하는 위치 N에 도달하면 출력 후 종료
#             print(idx)
#             exit(0)
#     idx += 1  # 다음 숫자로 이동

#------------------------------------------------------
# N = int(input())
#
# golomb = [0] * (N + 1)  # 골롱 수열 저장용 리스트
# golomb[1] = 1  # 초기값 설정
#
# # 골롱 수열을 미리 계산
# for i in range(2, N + 1):
#     golomb[i] = 1 + golomb[i - golomb[golomb[i - 1]]]
#
# print(golomb[N])

#------------------------------------------------------
# n = int(input())
#
# golomb = [0, 1, 2, 2]
# dp = [0] * (n+1)
# dp[1] = 1
# dp[2] = dp[3] = 2
#
# if n <= 1:
#     print(dp[n])
#     exit(0)
#
# for i in range(3, n+1):
#     for _ in range(golomb[i]):
#         golomb.append(i)
#     dp[i] = golomb[i]
#
# print(dp[n])