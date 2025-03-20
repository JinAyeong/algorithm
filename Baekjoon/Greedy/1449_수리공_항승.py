N, L = map(int, input().split())
waters = list(map(int, input().split()))
waters.sort()
tape = waters[0] + L
cnt = 1

for water in waters:
    if tape <= water:
        tape = water + L
        cnt += 1

print(cnt)