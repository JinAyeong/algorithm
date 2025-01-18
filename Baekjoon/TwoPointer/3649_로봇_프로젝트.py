# x: 너비, 레고조각 합: 구멍의 너비
import sys
input = sys.stdin.readline

while True:

    try:
        x = int(input()) * 10000000 # 구멍의 너비
        n = int(input()) # 레고 수
        lego = [int(input()) for _ in range(n)] # 10 이하
        lego.sort()

        result = False
        left = 0
        right = n-1

        if n == 0:
            print('danger')
            continue

        while left < right:

            length = lego[left] + lego[right]

            if length == x:
                print(f'yes {lego[left]} {lego[right]}')
                result = True
                break

            elif length > x:
                right -= 1

            elif length < x:
                left += 1

        if not result:
            print('danger')

    except:
        break