N = int(input())
K = int(input(), 2)
result = 0

while True:
    K = K - (K & ((~K)+1))
    result += 1
    if K == 0:
        break

print(result)