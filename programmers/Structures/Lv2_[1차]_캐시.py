from collections import deque

def solution(cacheSize, cities):
    answer = 0
    
    cache = deque([])
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        cur_city = city.lower()
        
        if cur_city not in cache:
            answer += 5
            
            if len(cache) == cacheSize:
                cache.popleft()
                
            cache.append(cur_city)
            
        else:
            answer += 1
            cache.remove(cur_city)
            cache.append(cur_city)
            
    return answer