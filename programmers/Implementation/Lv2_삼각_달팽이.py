'''
dir = 밑, 오른쪽, 위
'''

def solution(n):

    arr = [[0] * i for i in range(1, n+1)]
    arr[0][0] = 1
    
    dir = [(1, 0), (0, 1), (-1, -1)]
    r, c = 0, 0
    d = 0
    num = 2
    
    while num != n*(n+1) // 2 + 1:
        nr, nc = r + dir[d][0], c + dir[d][1]
        
        if 0 <= nr < n and nc <= nr and arr[nr][nc] == 0:
            arr[nr][nc] = num
            r, c = nr, nc
            num += 1
        else:
            d = (d+1) % 3
            
    answer = []
            
    for i in range(n):
        answer.extend(arr[i])
    
    return answer