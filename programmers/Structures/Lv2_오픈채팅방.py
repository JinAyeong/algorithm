'''
1. record 순서대로 split
2. change일 경우 닉네임 dict 수정
3. change가 아닐 경우 프린트
'''

def solution(record):
    answer = []
    nickname_dict = {}
    result = []
    
    for rec in record:
        data = rec.split()
        action = data[0]
        user_id = data[1]
        
        if action == 'Enter':
            nickname_dict[user_id] = data[2]
            result.append((action, user_id))
            
        elif action == 'Leave':
            result.append((action, user_id))
            
        elif action == 'Change':
            nickname_dict[user_id] = data[2]
    
    for action, user_id in result:
        if action == 'Enter':
            answer.append(f'{nickname_dict[user_id]}님이 들어왔습니다.')
        else:
            answer.append(f'{nickname_dict[user_id]}님이 나갔습니다.')
    
    return answer