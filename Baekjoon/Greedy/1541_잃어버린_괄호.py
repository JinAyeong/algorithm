arr = list(input().split('-'))

# '-'가 나오면 바로 괄호 열기, 다음 '-'가 나오면 괄호 닫기

result = 0
result += sum(map(int, arr[0].split('+')))

for str in arr[1:]:
    result -= sum(map(int, str.split('+')))

print(result)