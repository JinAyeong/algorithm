def solution(word):
    words = []
    
    def dfs(cur):
        if len(cur) > 5:
            return
        
        if cur:
            words.append(cur)
        
        for char in ['A', 'E', 'I', 'O', 'U']:
            dfs(cur + char)
    
    dfs("")
    
    return words.index(word) + 1