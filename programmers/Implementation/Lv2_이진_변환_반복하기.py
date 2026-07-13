def binary_trans(binary):
    cnt, cur_bin = 0, 0
    
    # 1. 0 제거
    cnt = binary.count("0")
    
    # 2. bin으로 변환
    cur_bin = bin(int(len(binary) - cnt))
    
    return cnt, cur_bin
    

def solution(s):
    answer = [0, 0]
    
    while s != "1":

        cur_cnt, cur_bin = binary_trans(str(s))
        s = cur_bin[2:]
        
        answer[1] += cur_cnt
        answer[0] += 1

    return answer