def solution(s):
    answer = ''
    sentence = s.split(" ")
    n = len(sentence)
    
    for idx, word in enumerate(sentence):
        answer += word[:1].upper() + word[1:].lower()
        if idx != n-1:
            answer += " "
    
    return answer