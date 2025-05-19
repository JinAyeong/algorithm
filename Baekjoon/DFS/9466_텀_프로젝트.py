'''
0번 학생부터 순회하며 연결 고리 찾기
'''

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(i):
    global cycle
    visited[i] = True
    path.append(i)
    next_student = students[i]

    if not visited[next_student]:
        dfs(next_student)
    else:
        if not finished[next_student]:
            cycle += path[path.index(next_student):]

    finished[i] = True

for _ in range(int(input())):
    n = int(input())
    students = list(map(lambda x: int(x) - 1, input().split()))
    visited = [False] * n
    finished = [False] * n
    cycle = []

    for i in range(n):
        if not visited[i]:
            path = []
            dfs(i)

    print(n - len(cycle))