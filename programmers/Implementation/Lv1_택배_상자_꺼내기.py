def solution(n, w, num):
    row = (num - 1) // w
    col = (num - 1) % w
    
    # row가 홀수면 col은 반대방향
    if row % 2 == 1:
        col = w - 1 - col
    
    count = 0
    total_rows = (n + w - 1) // w  # 총 층 수

    for r in range(row, total_rows):
        # 위층 방향 확인
        if r % 2 == 0:
            cur_col = col
        else:
            cur_col = w - 1 - col
        
        if r == total_rows - 1:
            last_count = n % w if n % w != 0 else w
            if cur_col >= last_count:
                break
        
        count += 1
    
    return count
