def solution(n):
    
    one_cnt = bin(n).count("1")
    next_num = n
    
    while True:
        next_num += 1
        if bin(next_num).count("1") == one_cnt:
            break
    
    return next_num