N = int(input())  # 재료수
M = int(input())  # 재료비
material = list(map(int, input().split()))
material.sort()

left = 0
right = N-1
result = 0

while left < right:

    if material[left] + material[right] == M:
        result += 1
        left += 1
        right -= 1
    elif material[left] + material[right] < M:
        left += 1
    elif material[left] + material[right] > M:
        right -= 1

print(result)