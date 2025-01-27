

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