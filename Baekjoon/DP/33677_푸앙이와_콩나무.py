'''
1: +1
3: *3
5: **2
'''

# python 48040 KB, 764 ms

N = int(input())
dp_water = [float('inf')] * (N+1)
dp_day = [float('inf')] * (N+1)
dp_water[0] = dp_day[0] = 0

def update(cur, next_pos, water_add):
    if next_pos >= N+1:
        return
    
    day = dp_day[cur] + 1
    water = dp_water[cur] + water_add

    if (dp_day[next_pos] > day or
        (dp_day[next_pos] == day and dp_water[next_pos] > water)):
        dp_day[next_pos] = day
        dp_water[next_pos] = water

for i in range(N):

    day = dp_day[i] + 1

    # 물 1만큼 주기
    update(i, i+1, 1)
    
    # 물 3만큼 주기
    update(i, i*3, 3)

    # 물 5만큼 주기
    update(i, i**2, 5)

print(dp_day[N], dp_water[N])

#########################################################################
# python 120096 KB, 1124 ms

N = int(input())
dp = [(float('inf'), 0)] * (N+1) # 일수, 물의 양
dp[0] = (0, 0)

for i in range(N):

    day = dp[i][0] + 1

    # 물 1만큼 주기
    if i+1 < N+1:
        water = dp[i][1] + 1
        if dp[i+1][0] > day:
            dp[i+1] = [day, water]
        elif dp[i+1][0] == day:
            if dp[i+1][1] > water:
                dp[i+1] = [day, water]
    
    # 물 3만큼 주기
    if i * 3 < N+1:
        water = dp[i][1] + 3
        if dp[i*3][0] > day:
            dp[i*3] = [day, water]
        elif dp[i*3][0] == day:
            if dp[i*3][1] > water:
                dp[i*3] = [day, water]

    # 물 5만큼 주기
    if i**2 < N+1:
        water = dp[i][1] + 5
        if dp[i**2][0] > day:
            dp[i**2] = [day, water]
        elif dp[i**2][0] == day:
            if dp[i**2][1] > water:
                dp[i**2] = [day, water]

print(*dp[N])