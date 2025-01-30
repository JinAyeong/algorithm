N = int(input())
solutions = list(map(int, input().split()))
solutions.sort()

left = 0
right = N-1
value = float('inf')
result = [0, 0]

while left < right:

    solution = solutions[left] + solutions[right]

    if solution < 0:
        if abs(solution) < value:
            result = [solutions[left], solutions[right]]
            value = abs(solution)
        left += 1

    elif solution > 0:
        if abs(solution) < value:
            result = [solutions[left], solutions[right]]
            value = abs(solution)
        right -= 1

    elif solution == 0:
        result = [solutions[left], solutions[right]]
        value = abs(solution)
        break

print(*result)