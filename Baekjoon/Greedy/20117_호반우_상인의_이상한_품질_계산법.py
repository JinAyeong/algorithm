'''
묶음이 짝수 -> 중앙값: (묶음개수 / 2 + 1)
묶음이 홀수 -> 중앙값: ((묶음개수 + 1) / 2)
길이가 2인 묶음으로 다 묶기
'''

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = sum(arr[(N+1)//2:]) * 2

if N % 2 == 1:
    result += arr[N//2]

print(result)