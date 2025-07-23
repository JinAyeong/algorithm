'''
수첩 1 : 연종이 하루동안 본 정수들
수첩 2 : 연종이 봤다고 대답한 수들
'''

T = int(input())

for _ in range(T):

    N = int(input())
    note_1 = list(map(int, input().split()))
    M = int(input())
    note_2 = list(map(int, input().split()))

    see = {}

    for num in note_1:
        see[num] = True

    for num in note_2:
        print(1 if num in see else 0)