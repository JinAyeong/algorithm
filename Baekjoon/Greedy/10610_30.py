'''
3의 배수이면서, 10의 배수
'''

N = list(input())

if '0' not in N:
    print(-1)

elif sum(map(int, N)) % 3 != 0:
    print(-1)

else:
    N.sort(reverse=True)
    print(''.join(N))