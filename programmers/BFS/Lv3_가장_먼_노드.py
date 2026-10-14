from collections import deque

def solution(n, edge):
    
    adjl = [[] for _ in range(n+1)]
    visited = [-1] * (n+1)
    
    for a, b in edge:
        adjl[a].append(b)
        adjl[b].append(a)
        
    q = deque([1])
    visited[1] = 0
    
    while q:
        
        cur_n = q.popleft()
        
        for next in adjl[cur_n]:
            if visited[next] == -1:
                visited[next] = visited[cur_n] + 1
                q.append(next)
    
    max_d = max(visited)
    answer = visited.count(max_d)
    
    return answer