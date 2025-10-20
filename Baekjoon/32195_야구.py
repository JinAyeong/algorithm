'''
파울, 내야, 홈런의 개수 구하기
N: 타구의 개수
x, y: 각 타구가 떨어진 지점
Q: 후보의 수
R: 담장까지의 거리로 고려되는 후보
'''
import sys
input = sys.stdin.readline

N = int(input())
spots = [list(map(int, input().split())) for _ in range(N)]

for _ in range(int(input())):
    R = int(input())

    foul = inyard = homerun = 0

    for x, y in spots:

        # 내야일 경우
        if x**2 + y**2 <= R**2 and y >= x and y >= -x:
            inyard += 1
        
        # 홈런일 경우
        elif x**2 + y**2 >= R**2 and y >= x and y >= -x:
            homerun += 1
        
        else:
            foul += 1

    print(foul, inyard, homerun)
