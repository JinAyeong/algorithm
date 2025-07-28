n = int(input())
numbers = list(map(int, input().split()))
x = int(input())
numbers.sort()

answer = 0

left = 0
right = n-1

while left < right:
    num1 = numbers[left]
    num2 = numbers[right]

    if num1 + num2 == x:
        answer += 1
        left += 1
        right -= 1

    elif num1 + num2 < x:
        left += 1

    elif num1 + num2 > x:
        right -= 1

print(answer)