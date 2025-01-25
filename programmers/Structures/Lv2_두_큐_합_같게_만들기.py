# pop, push -> 작업 1회
from collections import deque


def solution(queue1, queue2):
    n = len(queue1)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    result = 0

    while sum1 != sum2:

        if result == n * 3: # 큐 한바퀴 돌아서 제자리
            result = -1
            break

        if sum1 > sum2:
            num = queue1.popleft()
            queue2.append(num)
            sum1 -= num
            sum2 += num
            result += 1

        elif sum1 < sum2:
            num = queue2.popleft()
            queue1.append(num)
            sum2 -= num
            sum1 += num
            result += 1

    return result


#------------------------------------------
# 실패 코드
# pop, push -> 작업 1회
from collections import deque


def solution(queue1, queue2):
    n = len(queue1)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    result = 0

    while sum1 != sum2:

        if sum1 == 0 or sum2 == 0: # 무한 루프
            result = -1
            break

        if sum1 > sum2:
            num = queue1.popleft()
            queue2.append(num)
            sum1 -= num
            sum2 += num
            result += 1

        elif sum1 < sum2:
            num = queue2.popleft()
            queue1.append(num)
            sum2 -= num
            sum1 += num
            result += 1

    return result