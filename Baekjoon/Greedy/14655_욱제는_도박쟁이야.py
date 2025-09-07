'''
첫번쨰 라운드 : 동전에 표시된 값들의 합이 최대
두번째 라운드 : 동전에 표시된 값들의 합이 최소
획득점수 = 첫번쨰 라운드 - 두번째 라운드

욱제의 동전 뒤집기
- 연속한 3개의 동전 뒤집기
- 양끝은 두개 또는 한개만 뒤집어도 가능
'''

N = int(input())
first = list(map(lambda x: abs(int(x)), input().split()))
second = list(map(lambda x: abs(int(x)), input().split()))

answer = sum(first) + sum(second)
print(answer)