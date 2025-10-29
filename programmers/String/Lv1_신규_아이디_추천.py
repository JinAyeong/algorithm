def solution(new_id):
    
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    for char in new_id:
        if not char.isalpha() and not char.isdigit() and char not in ['-', '_', '.']:
            new_id = new_id.replace(char, "")
    
    # 3단계
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    
    # 4단계
    new_id = new_id.strip('.')
    
    # 5단계
    if not new_id:
        new_id = 'a'
    
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15].rstrip('.')
    
    # 7단계
    while len(new_id) < 3:
        new_id += new_id[-1]
    
    return new_id
