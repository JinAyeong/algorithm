'''
1. -가 3^N개 있는 문자열에서 시작
2. 문자열 3등분
3. 가울데 문자열 = 공백
4. 위의 과정 모든 선의 길이가 1이 될 때 까지 반복
'''

import sys

def dfs(i, j):

    if j - i == 1:
        return

    for k in range(i + (j - i) // 3, i + (j - i) // 3 * 2):
        string[k] = ' '

    dfs(i, i + (j - i) // 3)
    dfs(i + (j - i) // 3 * 2, j)

for line in sys.stdin:
    N = int(line)
    string = ['-'] * (3**N)
    dfs(0, 3**N)
    print("".join(string))