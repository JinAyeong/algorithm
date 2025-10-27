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