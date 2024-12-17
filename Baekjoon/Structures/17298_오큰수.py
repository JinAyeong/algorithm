# NGE(i) = 오른쪽에 있으면서 Ai보다 큰 수중에 가장 왼쪽에 있는 수
# 없을경우엔 NGE(i) = -1

# 1. range(N-1, -1, -1) 순회하면서 가장 끝 값부터 검사
# 2. stack = [numbers[-1]]로 시작
# 3. 순회하면서 stack[-1]과 비교하여 오큰수인지 확인
# 3-1. 오큰수가 맞다면 현재 값도 append하고 result[i]에 오큰수 저장
# 3-2. 오큰수가 아니라면 stack.pop() (어차피 앞으로 순회할 값의 오큰수도 되지 못함, pop해서 제거)
# 4. stack이 비어있으면 오큰수 찾지 못했을 경우이므로 result[i]에 -1 저장

N = int(input())
numbers = list(map(int, input().split()))
stack = []

result = [0] * N

for i in range(N-1, -1, -1):

    cur = numbers[i]

    # 오큰수가 될 수 없는 값들 제거
    while stack:

        # 현재 값의 오큰수가 아님 = 이후 순회할 숫자들의 오큰수도 될 수 없음 -> pop하여 제거
        if cur >= stack[-1]:
            stack.pop()
        # 오큰수 찾음 -> break
        else:
            break

    # 오큰수 결정
    if stack:
        result[i] = stack[-1]
    else:
        result[i] = -1

    # while문 끝나면 stack에 현재 값 무조건 추가
    stack.append(cur)

print(*result)