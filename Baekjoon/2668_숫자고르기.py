N = int(input())
numbers = [0] * (N+1)
used = [0] * (N+1)

for i in range(1, 1+N):
    num = int(input())
    numbers[i] = num

def move(cur, arr):

    if numbers[cur] == cur:
        # 싸이클 생김
        return arr