N, M = map(int, input().split())

result = 0

def choice(i, lst):
    global result

    if i == N+1:
        result += 1

    for j in range(1, 1+N):
        if j not in lst and