def solution(files):
    
    def sort_by(file):
        
        n = len(file)
        
        # 1. head
        
        n_idx = 0
        
        for f in range(n):
            
            if file[f].isdigit():
                break
                
            n_idx += 1
                
        head = file[:n_idx]
        
        # 2. number
        
        t_idx = n_idx
        
        for f in range(n_idx, n):
            
            if not file[f].isdigit():
                break
                
            t_idx += 1
                
        number = file[n_idx:t_idx]
        
        return head.lower(), int(number)
        
    
    answer = sorted(files, key = sort_by)
    return answer