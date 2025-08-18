R, C = map(int, input().split())
mp = [list(input()) for _ in range(R)]
answer = [0] * 10

grade = 1

for i in range(C-2, 0, -1):
    is_found = False
    for j in range(R):
        if mp[j][i] != '.' and answer[int(mp[j][i])] == 0:
            answer[int(mp[j][i])] = grade
            is_found = True
    if is_found:
        grade += 1

for a in answer:
    if a == 0:
        continue
    print(a)