from collections import deque

for tc in range(int(input())):

    p = input()  # 수행할 함수
    n = int(input())   # 배열의 길이

    arr = list(map(str, input().split(",")))
    arr[0] = arr[0][1:]
    arr[-1] = arr[-1][:-1]
    new_arr = deque(arr)

    reversed_state = False
    result = True

    for cur in p:

        if cur == 'D':
            if new_arr and new_arr != deque(['']):
                if not reversed_state:
                    new_arr.popleft()
                else:
                    new_arr.pop()
            else:
                result = False
                break

        elif cur == 'R':
            reversed_state = not reversed_state

    if result and reversed_state:
        new_arr.reverse()

    if result:
        print("[" + ",".join(new_arr) + "]")

    else:
        print('error')