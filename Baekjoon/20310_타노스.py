# 문자열의 순서 바꾸면 안됨 -> 주어진 순서에서 pop 하듯이 삭제 가능

from collections import defaultdict

S = input()
char = defaultdict(int)

for s in S:
    char[s] += 1

