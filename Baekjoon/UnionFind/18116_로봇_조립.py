'''
I a b : a, b가 같은 로봇의 부품
Q c : 지금까지 알아낸 c의 부품이 몇 개냐는 의미
'''

import sys
input = sys.stdin.readline

N = int(input())
parent = [i for i in range(10**6 + 1)]
size = [1 for _ in range(10**6 + 1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):

    rootX = find(x)
    rootY = find(y)

    if rootX != rootY:
        if size[rootX] > size[rootY]:
            size[rootX] += size[rootY]
            parent[rootY] = rootX
        else:
            size[rootY] += size[rootX]
            parent[rootX] = rootY

for _ in range(N):
    question, *number = list(input().split())

    if question == 'I':
        union(int(number[0]), int(number[1]))
    elif question == 'Q':
        print(size[find(int(number[0]))])