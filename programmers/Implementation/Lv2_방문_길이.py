def solution(dirs):
    answer = 0
    direction = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}
    visited = set()
    cr, cc = 5, 5
    
    for dir in dirs:
        dr, dc = direction[dir]
        nr, nc = cr + dr, cc + dc
        
        if 0 <= nr < 11 and 0 <= nc < 11:
            if ((nr, nc), (cr, cc)) not in visited and ((cr, cc), (nr, nc)) not in visited:
                visited.add(((nr, nc), (cr, cc)))
                visited.add(((cr, cc), (nr, nc)))
                answer += 1
            cr, cc = nr, nc
            
    return answer