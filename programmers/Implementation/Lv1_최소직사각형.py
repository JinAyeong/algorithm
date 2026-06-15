def solution(sizes):
    
    for size in sizes:
        size.sort()
    
    height = max(size[0] for size in sizes)
    width = max(size[1] for size in sizes)
    answer = height * width
    
    return answer