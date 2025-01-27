# sys.stdin.readline은 줄바꿈을 포함해서 입력 받기 때문에 /n이 포함되어 값이 달라짐
# rstip 메서드 적용 : 입력 뒤에 있는 공백이나 줄바꿈을 다 지워줌

import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())  # 메모장에 적은 키워드, 블로그에 쓴 글의 수
memo = dict()
result = N

for _ in range(N):
    word = input().rstrip()
    if word not in memo:
        memo[word] = True

for _ in range(M):
    keywords = list(input().rstrip().split(','))

    for keyword in keywords:
        if keyword in memo and memo[keyword]:
            memo[keyword] = False
            result -= 1

    print(result)