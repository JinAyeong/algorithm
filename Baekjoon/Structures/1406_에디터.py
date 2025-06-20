from collections import deque

string_1 = deque(input())
string_2 = deque([])
M = int(input())

for _ in range(M):
    P, *s = input().split()

    if P == 'L' and string_1:
        char = string_1.pop()
        string_2.appendleft(char)

    elif P == 'D' and string_2:
        char = string_2.popleft()
        string_1.append(char)

    elif P == 'B' and string_1:
        string_1.pop()

    elif P == 'P':
        string_1.append(*s)

print("".join(string_1), end="")
print("".join(string_2))