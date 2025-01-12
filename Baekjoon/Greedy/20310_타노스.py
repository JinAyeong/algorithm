# 문자열의 순서 바꾸면 안됨 -> 주어진 순서에서 pop 하듯이 삭제 가능
# 순서대로 순회하면서
# 1이 나올때 : 갯수의 반절만큼 무시했으면 append 아니면 무시
# 0이 나올때 : 갯수 다 안찼으면 append 아니면 무시

from collections import defaultdict

S = input()
char = defaultdict(int)
result = ''

for s in S:
    char[s] += 1

append_0 = 0
pass_1 = 0

for s in S:

    if s == '0' and append_0 < char['0'] // 2:
        result += s
        append_0 += 1

    if s == '1' and pass_1 >= char['1'] // 2:
        result += s
    elif s == '1' and pass_1 < char['1'] // 2:
        pass_1 += 1

print(result)