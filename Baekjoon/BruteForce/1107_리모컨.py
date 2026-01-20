# Bruteforce

N = int(input()) # 이동할 채널
M = int(input()) # 고장난 버튼 수

if N == 100:
    print(0)
    exit(0)

if M == 0:
    error_button = []
else:
    error_button = list(input().split())

num_lst = []
result = abs(100 - N)


# 리모콘 숫자버튼으로 이동할 수 있는 모든 채널 구하기
for i in range(1000001):

    s = str(i)
    can_use = True

    for j in range(len(s)):
        if s[j] in error_button:
            can_use = False
            break

    if can_use:
        num_lst.append((s, len(s)))

# 숫자버튼으로 이동할 수 있는 채널 중 + 또는 - 버튼으로 목표 채널에 도달하려면 누를 버튼 수 계산하여 결과 갱신
for num, cnt in num_lst:

    if abs(int(num) - N) + cnt < result:
        result = abs(int(num) - N) + cnt

print(result)