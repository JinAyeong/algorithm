N = int(input())
fruits = list(map(int, input().split()))

used = [0] * 10
left = 0
right = 0
used[fruits[0]] += 1
cur_num = 1
max_num = 1

for _ in range(N-1):

    # 과일 추가
    right += 1
    used[fruits[right]] += 1
    cur_num += 1

    fruit_num = 10 - used.count(0)

    # 과일 검사 후 두종류 넘어가면 과일 빼기
    if fruit_num > 2:
        used[fruits[left]] -= 1
        left += 1
        cur_num -= 1

    # 최댓값 검사
    if 10 - used.count(0) <= 2 and cur_num > max_num:
        max_num = cur_num


print(max_num)