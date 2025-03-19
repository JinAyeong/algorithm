N = int(input())
colors = input()
result = 0

while len(colors) > 0:
    left = colors[0]
    right = colors[-1]

    if left == right:
        colors = colors.rstrip(right)
        colors = colors.lstrip(left)

    else:
        colors = colors.rstrip(right)

    result += 1

print(result)
