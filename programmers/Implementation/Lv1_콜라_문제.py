def solution(a, b, n):  # 콜라 a개 가져다 주면 b개 받을 수 있을때, n개 가져다줬을때 받을 수 있는 콜라의 수
    answer = 0

    while n >= a:
        benefit = (n // a) * b
        answer += benefit
        n -= n // a * a
        n += benefit

    return answer