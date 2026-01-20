'''
n개의 나무, n일 등산
나무 성장 모아두기
'''

n = int(input())
trees = list(map(int, input().split()))
growth = list(map(int, input().split()))

data = list(zip(growth, trees))
data.sort()

answer = 0

for day, (g, h) in enumerate(data):
    answer += h + g * day

print(answer)
