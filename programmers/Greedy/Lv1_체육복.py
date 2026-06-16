def solution(n, lost, reserve):
    
    lost_set = set(lost)
    reserve_set = set(reserve)

    lost = lost_set - reserve_set
    reserve = reserve_set - lost_set

    for r in sorted(reserve):
        if r - 1 in lost:
            lost.remove(r - 1)
        elif r + 1 in lost:
            lost.remove(r + 1)

    return n - len(lost)