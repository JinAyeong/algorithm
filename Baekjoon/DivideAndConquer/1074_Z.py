'''
해당 구역까지 찾아가서 조금씩 숫자를 더하기
'''

N, r, c = map(int, input().split())

result = 0

def z(n, r, c, x, y):
    global result

    if n == 1:
        print(result)
        return

    half = n // 2

    # 0
    if r < x + half and c < y + half:
        z(half, r, c, x, y)

    # 1
    elif r < x + half and c >= y + half:
        result += half * half
        z(half, r, c, x, y + half)

    # 2
    elif r >= x + half and c < y + half:
        result += half * half * 2
        z(half, r, c, x + half, y)

    # 3
    else:
        result += half * half * 3
        z(half, r, c, x + half, y + half)

z(2**N, r, c, 0, 0)
