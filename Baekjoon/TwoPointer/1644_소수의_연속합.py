N = int(input())

def prime(n):

    numbers = [True] * (n+1)
    numbers[0] = numbers[1] = False

    for i in range(2, n+1):

        if numbers[i]:
            for j in range(2 * i, n+1, i):
                numbers[j] = False

    return [k for k in range(n+1) if numbers[k]]

prime_lst = prime(N)
left = 0
right = 0
cur = 0
cnt = 0

while left <= right <= len(prime_lst):
    if cur == N:
        cnt += 1

    if cur <= N:
        if right == len(prime_lst):
            break
        cur += prime_lst[right]
        right += 1

    elif cur > N:
        cur -= prime_lst[left]
        left += 1

print(cnt)