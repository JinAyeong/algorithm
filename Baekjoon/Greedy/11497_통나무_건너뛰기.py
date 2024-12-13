# 난이도 : 인접한 두 통나무 간의 높이 차의 최댓값
# result = 주어진 통나무로 만들 수 있는 최소 난이도
# 0, 2, 4, 3, 1 순으로 출력

for tc in range(int(input())):

    N = int(input()) # 통나무 수
    logs = list(map(int, input().split())) # 통나무 배열
    logs.sort()

    logs_even = []
    logs_odd = []

    # 통나무 배열
    for i in range(N):
        
        if i % 2 == 0:
            logs_even.append(logs[i])

        else:
            logs_odd.append(logs[i])

    logs_odd.reverse()

    result_arr = logs_even + logs_odd

    max_jump = 0

    for l in range(N):

        max_jump = max(max_jump, abs(result_arr[l] - result_arr[l-1]))

    print(max_jump)