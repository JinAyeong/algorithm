T = int(input()) # 문자열 수

for _ in range(T):

    word = input()
    left = 0
    right = len(word) - 1
    result = 0
    cnt = 0 # 문자열 안맞은 횟수

    index = []

    while left <= right:

        if word[left] == word[right]:
            left += 1
            right -= 1

        # 문자열 안맞은게 처음이라면 : 왼쪽 문자열을 삭제해보기
        elif result == 0:
            result = 1
            index = [left, right]
            left += 1
            cnt += 1

        # 문자열 안맞은게 두번째라면 : 처음안맞았던 부분으로 돌아가서 오르쪽 문자열 삭제해보기
        elif result == 1 and cnt == 1:
            left = index[0]
            right = index[1] - 1
            cnt += 1

        # 문자열 안맞은게 세번째라면 : 회문 만들 수 없음
        elif result == 1 and cnt == 2:
            result = 2
            break

    print(result)