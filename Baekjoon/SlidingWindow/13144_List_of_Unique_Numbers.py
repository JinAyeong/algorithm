N = int(input())
numbers = list(map(int, input().split()))

select = set()
start = 0
result = 0

for end in range(N):

    while numbers[end] in select:
        select.remove(numbers[start])
        start += 1

    select.add(numbers[end])
    result += (end - start + 1)

print(result)