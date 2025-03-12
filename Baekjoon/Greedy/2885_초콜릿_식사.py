K = int(input())
size = 1
cnt = 0
eat = 0

while size < K:
    size *= 2

print(size, end=" ")

if size != K:

    while eat != K:
        size //= 2
        cnt += 1
        if size <= K - eat:
            eat += size

print(cnt)