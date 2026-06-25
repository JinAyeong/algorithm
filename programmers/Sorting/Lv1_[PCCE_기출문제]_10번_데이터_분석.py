'''
data에서 ext값이 val_ext보다 작은 데이터를 sort_by를 기준으로 오름차순 정렬
'''

def solution(data, ext, val_ext, sort_by):
    
    column_idx = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}
    answer = []
    
    for d in data:
        if d[column_idx[ext]] < val_ext:
            answer.append(d)
    
    answer.sort(key = lambda x: x[column_idx[sort_by]])
    
    return answer