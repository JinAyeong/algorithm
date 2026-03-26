'''
하루에 과제 한개 끝내기 가능
과제마다 마감일 존재
점수 최대값 구하기
'''

N = int(input())
assignments = [tuple(map(int, input().split())) for _ in range(N)]
assignments.sort(key = lambda x: (-x[1], x[0]))
day = [0] * 1001

for due, score in assignments:
    for d in range(due, 0, -1):
        if not day[d]:
            day[d] = score
            break

print(sum(day))