'''
2변 이상이 닿으면 녹아 없어짐
한시간 지나면 치즈 내부에 공기 유입
치즈 모두 녹는데 걸리는 시간 구하기
'''

N, M = map(int, input().split()) # 세로, 가로
mp = [list(map(int, input().split())) for _ in range(N)]

# def bfs():
    
