# 나의 순위 : 나보다 높은 점수를 받은 팀의 수 + 1
# 동점자 순위
# - 점수가 같은 경우 : 제출 횟수가 적은 팀이 높은 순위
# - 제춣 횟수도 같은 경우 : 마지막 제출 시간이 더 빠르 팀이 높은 순위

for _ in range(int(input())):

    n, k, t, m = map(int, input().split()) # 팀 수, 문제 수, 내 ID, 로그 수

    logs = [[{}, 0, 0, id] for id in range(n+1)] # 문제별 총점, 제출 횟수, 마지막 제출, id

    for sub in range(m):

        i, j, s = map(int, input().split()) # id, 문제 번호, 점수

        # 문제 점수 갱신
        if j not in logs[i][0]:
            logs[i][0][j] = s

        else:
            logs[i][0][j] = max(logs[i][0][j], s)

        logs[i][1] += 1 # 제출 횟수 += 1

        logs[i][2] = sub # 마지막 제출

    # 총점 계산
    logs = list(map(lambda x: [sum(x[0].values()), x[1], x[2], x[3]], logs))

    # 정렬
    logs.sort(key=lambda x:(-x[0], x[1], x[2]))

    # 내 등수 찾기
    for idx, log in enumerate(logs):
        if log[3] == t:
            print(idx + 1)
            break