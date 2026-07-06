def solution(n, words):
    used = {words[0]}

    for idx, word in enumerate(words):
        
        if idx == 0:
            continue
            
        if word not in used and word[0] == words[idx-1][-1]:
            used.add(word)
            continue
        
        return [idx % n + 1, idx // n + 1]

    return [0, 0]