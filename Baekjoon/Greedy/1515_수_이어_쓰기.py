num = input()
N = 1
index = 0

# 철자 다 탐색할때까지
while index < len(num):

    # 현재 검새하는 숫자의 길이만큼 순회
    for n in range(len(str(N))):
        # 현재 수 == 전체 길이의 지금 인덱스 이면 다음 인덱스로, 안맞으면 패스
        if str(N)[n] == num[index]:
            index += 1

            if index >= len(num):
                break

    N += 1

print(N-1)