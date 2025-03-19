# 투포인터
# python 33392 KB 180 ms

N = int(input())
colors = input()
left, right = 0, N - 1
result = 0

while left <= right:
    if colors[left] == colors[right]:
        char = colors[left]
        while left <= right and colors[left] == char:
            left += 1
        while left <= right and colors[right] == char:
            right -= 1
    else:
        char = colors[right]
        while left <= right and colors[right] == char:
            right -= 1

    result += 1

print(result)

#-------------------------------------------------------
# 문자열
# python 33392 KB 1756 ms
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
