#############################################################
# prefix로 저장
def solution(mats, park):
    mats.sort(reverse=True)
    r, c = len(park), len(park[0])
    grid = [[0 if park[i][j] == '-1' else 1 for j in range(c)] for i in range(r)]

    # 누적합 배열
    prefix = [[0]*(c+1) for _ in range(r+1)]
    for i in range(1, r+1):
        for j in range(1, c+1):
            prefix[i][j] = grid[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

    # 매트 크기별 검사
    for mat in mats:
        for i in range(r - mat + 1):
            for j in range(c - mat + 1):
                total = prefix[i+mat][j+mat] - prefix[i][j+mat] - prefix[i+mat][j] + prefix[i][j]
                if total == 0:
                    return mat
    return -1


#############################################################
# 모든 열마다 검사

def check(length, park, i, j):
    
    for a in range(i, i+length):
        for b in range(j, j+length):
            if park[a][b] != '-1':
                return False
    return True

def solution(mats, park):
    mats.sort(reverse = True)
    r, c = len(park), len(park[0])
    
    for mat in mats:
        for i in range(0, r-mat+1):
            for j in range(0, c-mat+1):
                if check(mat, park, i, j):
                    return mat
    
    return -1