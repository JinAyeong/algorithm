'''
1. 제일 위에 있는 카드 바닥에 버리기
2. 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮기기
'''

from collections import deque

N = int(input())

cards = deque(range(1, N+1))
discarded = []

while len(cards) > 1:

    discarded.append(cards.popleft())

    if len(cards) == 1:
        break

    cards.append(cards.popleft())

print(*discarded, *cards)