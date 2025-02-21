N = int(input())
solutions = list(map(int, input().split()))
solutions.sort()

left = 0
right = N-1
min_result = float('inf')
solution_result = [0, 0]

while left < right:

    solution = solutions[left] + solutions[right]

    if abs(solution) <= min_result:
        min_result = abs(solution)
        solution_result[0] = solutions[left]
        solution_result[1] = solutions[right]

    if solution == 0:
        break

    elif solution < 0:
        left += 1

    elif solution > 0:
        right -= 1

print(*solution_result)