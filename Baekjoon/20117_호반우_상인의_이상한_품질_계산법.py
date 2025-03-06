'''
묶음이 짝수 -> 중앙값: (묶음개수 / 2 + 1)
묶음이 홀수 -> 중앙값: ((묶음개수 + 1) / 2)
'''

def middle(n):
    if n % 2 == 0:
        return (n // 2) + 1
    else:
        return (n + 1) // 2


N = int(input())
arr = list(map(int, input().split()))
arr.sort()

