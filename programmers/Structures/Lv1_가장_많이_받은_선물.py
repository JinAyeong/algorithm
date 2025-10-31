from itertools import combinations

def give_count(idx, grid):
    return sum(grid[idx])

def receive_count(idx, grid, n):
    return sum(grid[i][idx] for i in range(n))

def solution(friends, gifts):
    n = len(friends)
    friends_idx = {friend: idx for idx, friend in enumerate(friends)}
    
    # 선물 주고받은 수
    grid = [[0] * n for _ in range(n)]
    
    for gift in gifts:
        give, receive = gift.split()
        give_idx, receive_idx = friends_idx[give], friends_idx[receive]
        grid[give_idx][receive_idx] += 1
        
    # 선물지수
    gift_score = {
        friend: give_count(idx, grid) - receive_count(idx, grid, n)
        for idx, friend in enumerate(friends)
    }
    
    # 다음달 선물 받을 수
    next_month_gift = {friend: 0 for friend in friends}
    
    for f1, f2 in combinations(friends, 2):
        f1_idx, f2_idx = friends_idx[f1], friends_idx[f2]
        
        if grid[f1_idx][f2_idx] < grid[f2_idx][f1_idx]:
            next_month_gift[f2] += 1
        elif grid[f1_idx][f2_idx] > grid[f2_idx][f1_idx]:
            next_month_gift[f1] += 1
        else:
            if gift_score[f1] > gift_score[f2]:
                next_month_gift[f1] += 1
            elif gift_score[f2] > gift_score[f1]:
                next_month_gift[f2] += 1
    
    return max(next_month_gift.values())