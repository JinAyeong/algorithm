N = int(input())
solutions = list(map(int, input().split()))

left, right = 0, N-1
result = float('inf')
result_ph = [0, 0]
result_index = [0, N-1]

while left < right:

    solution = solutions[left] + solutions[right]

    if abs(solution) < result:
        result = abs(solution)
        result_ph[0], result_ph[1] = solutions[left], solutions[right]
        result_index[0], result_index[1] = left, right

        left += 1

    # elif abs(solution) > result:

