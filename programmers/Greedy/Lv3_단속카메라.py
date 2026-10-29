def solution(routes):
    answer = 1
    
    routes.sort()
    ce = routes[0][1]
    
    for s, e in routes:
        if s <= ce and e <= ce:
            ce = e
        elif s > ce:
            ce = e
            answer += 1
    
    return answer