N = int(input())
weights = list(map(int, input().split()))
weights.sort()

num = 1

for weight in weights:
    if weight > num:
        break
    num += weight

print(num)