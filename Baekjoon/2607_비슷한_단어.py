from collections import Counter

n = int(input())
words = [input().strip() for _ in range(n)]
base = Counter(words[0])
count = 0

for word in words[1:]:
    comp = Counter(word)
    diff = 0

    # 두 Counter의 차이 합계 구하기
    for c in set(base.keys() | comp.keys()):
        diff += abs(base[c] - comp[c])

    # 조건 만족하는 경우
    if diff <= 1 or (diff == 2 and len(base) == len(comp)):
        count += 1

print(count)
