def solution(s):
    answer = []
    
    s = list(s[2:-2].split('},{'))
    s.sort(key = lambda s: len(s))
    
    for tup in s:
        cur_tup = tup.split(',')
        for char in cur_tup:
            if int(char) not in answer:
                answer.append(int(char))
    
    return answer