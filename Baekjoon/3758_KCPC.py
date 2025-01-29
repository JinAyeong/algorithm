# 나의 순위 : 나보다 높은 점수를 받은 팀의 수 + 1
# 동점자 순위
# - 점수가 같은 경우 : 제출 횟수가 적은 팀이 높은 순위
# - 제춣 횟수도 같은 경우 : 마지막 제출 시간이 더 빠르 팀이 높은 순위
from collections import defaultdict

for _ in range(int(input())):

    logs = []

    n, k, t, m = map(int, input().split()) # 팀 수, 문제 수, 나의 Id, 로그 엔트리 수

    for sub in range(m):
        i, j, s = map(int, input().split()) # 팀 ID, 문제 번호, 획득 점수

        logs.append((i, j, -s, sub)) # ID, 문제 번호, 획득 점수, 제출 순서

    logs.sort()

    sorted_logs = []

    for i, j, s, sub in logs:
