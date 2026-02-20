'''
- 1부터 n까지의 수 stack에 push
- push하는 도중, pop -> 수열 만들기
'''

n = int(input())
stack = []
current = 1
result = []
possible = True

for _ in range(n):
    num = int(input())

    # 원하는 num이 나올 때 까지 push
    while current <= num:
        stack.append(current)
        result.append('+')
        current += 1

    # 스택 top이 num이면 pop
    if stack and stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        possible = False
        break

if possible:
    print('\n'.join(result))
else:
    print("NO")