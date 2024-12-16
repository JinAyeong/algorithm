# NGE(i) = 오른쪽에 있으면서 Ai보다 큰 수중에 가장 왼쪽에 있는 수
# 없을경우엔 NGE(i) = -1

N = int(input())
sequence = list(map(int, input().split()))

max_num = sequence[-1]

for i in range(N-1, -1, -1):

    if i == len(sequence) - 1:
        print(-1, end=" ")

    else:
        if max_num > sequence[i]:
            print(max_num, end=" ")

    # 숫자 갱신 우와!
    if sequence[i] > sequence[i-1]:
        max_num = sequence[i]

    print('a')