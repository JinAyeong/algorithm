N = int(input())
answer = list(input().split())
hyunwoo = list(input().split())

cnt = N * (N-1) // 2

# 순서 인덱스
answer_index = {}
hyunwoo_index = {}

for idx, value in enumerate(answer):
    answer_index[value] = idx

for idx, value in enumerate(hyunwoo):
    hyunwoo_index[value] = idx


def grading(a, b):
    if answer_index[a] < answer_index[b] and hyunwoo_index[a] < hyunwoo_index[b]:
        return True

    if answer_index[a] > answer_index[b] and hyunwoo_index[a] > hyunwoo_index[b]:
        return True

    return False

used = [False] * N
score = 0

def comb(i, start, choose):

    global score

    if i == 2:
        if grading(choose[0], choose[1]):
            score += 1
        return

    for j in range(start, N):
        comb(i + 1, j + 1, choose + [hyunwoo[j]])

comb(0, 0, [])

print(f'{score}/{cnt}')