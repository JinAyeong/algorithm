'''
회원자격 : 10일동안 부여
할인제품 : 하루에 한 개 구매 가능
'''

from collections import Counter

def solution(want, number, discount):
    target = dict(zip(want, number))
    window = Counter(discount[:10])

    answer = int(window == target)

    for i in range(10, len(discount)):
        window[discount[i - 10]] -= 1
        
        if window[discount[i - 10]] == 0:
            del window[discount[i - 10]]

        window[discount[i]] += 1

        answer += (window == target)

    return answer