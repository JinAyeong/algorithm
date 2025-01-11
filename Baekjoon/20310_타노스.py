from collections import defaultdict

S = input()
char = defaultdict(int)

for s in S:
    char[s] += 1

result = '0' * (char['0'] // 2) + '1' * (char['1'] // 2)

print(result)