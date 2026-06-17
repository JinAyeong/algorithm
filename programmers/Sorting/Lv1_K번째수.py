def solution(array, commands):
    answer = []
    
    def k_sort(i, j, k):
        
        new_array = sorted(array[i-1:j])
        return new_array[k-1]
    
    for i, j, k in commands:
        
        answer.append(k_sort(i, j, k))
    
    return answer