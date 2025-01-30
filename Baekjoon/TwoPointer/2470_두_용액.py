N = int(input())
solutions = list(map(int, input().split()))
solutions.sort()

left = 0
right = N-1
value = float('inf')
result = [0, 0]

while left < right:

    solution = solutions[left] + solutions[right]

    # 결과 먼저 갱신
    if abs(solution) < value:
        result = [solutions[left], solutions[right]]
        value = abs(solution)

    # 0에 가까워지도록 포인터 조절
    if solution < 0:
        left += 1

    elif solution > 0:
        right -= 1

    elif solution == 0:
        break

print(*result)