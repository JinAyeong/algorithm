N, M = map(int, input().split())
scores = list(map(int, input().split()))
grade = []

for _ in range(M):
    num, *answers = input().split()
    cur_score = sum(scores[s] for s in range(N) if answers[s] == 'O')
    grade.append((int(num), cur_score))

grade.sort(key=lambda x:[-x[1], x[0]])
print(*grade[0])