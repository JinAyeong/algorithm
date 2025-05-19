'''
0번 학생부터 순회하며 연결 고리 찾기
'''

# python 60704 KB, 2832 ms

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(i):
    global result

    visited[i] = True
    next = students[i]

    if not visited[next]:
        dfs(next)
    elif not finished[next]:
        j = next  # 현재 사이클 발생한 학생 번호 : j
        while j != i:  # 다시 경로 탐색하면서 그 사이클 길이 카운트 하기
            result += 1
            j = students[j]
        result += 1

    finished[i] = True


for _ in range(int(input())):
    n = int(input())
    students = list(map(lambda x: int(x) - 1, input().split()))
    visited = [False] * n
    finished = [False] * n
    result = 0

    for i in range(n):
        if not visited[i]:
            dfs(i)

    print(n - result)

#-----------------------------------------------------------------------------------------------
# python 62312 KB, 3552 ms
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(i):
    global cycle
    visited[i] = True
    path.append(i)
    next_student = students[i]     # i 학생이 선호하는 학생 번호

    if not visited[next_student]:  # 다음 학생이 아직 dfs 탐색하지 않은 학생일 경우 dfs 탐색
        dfs(next_student)
    elif not finished[next_student]:              # 다음학생 dfs 탐색 시작했고, 아직 완료되지 않았을 경우
        cycle += path[path.index(next_student):]  # 사이클이 생긴 학생들만 팀을 이룬 학생 배열에 추가

    finished[i] = True  # dfs 완료 표시

for _ in range(int(input())):
    n = int(input())
    students = list(map(lambda x: int(x) - 1, input().split()))
    visited = [False] * n   # 아직 방문하지 않은 노드를 대상으로만 dfs 시작
    finished = [False] * n  # 사이클 여부 판단 시, 이미 사이클을 판별한 노드인지 확인할 때 사용
    cycle = []              # 팀을 이룬 학생들 번호

    for i in range(n):
        if not visited[i]:
            path = []   # dfs 탐색을 하며 연결된 학생들 배열
            dfs(i)

    print(n - len(cycle))