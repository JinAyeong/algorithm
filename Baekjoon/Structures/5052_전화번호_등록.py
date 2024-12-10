for tc in range(int(input())):

    n = int(input())   # 전화번호 수

    numbers = [input() for _ in range(n)]

    numbers.sort()  # 전화번호 사전순 정렬

    result = 'YES'

    for i in range(n-1):
        
        if len(numbers[i]) > len(numbers[i+1]):
            continue

        if numbers[i] == numbers[i+1][:len(numbers[i])]:
            result = 'NO'
            break
        
        # 또는
        # 접두어 확인 메서드 : startswitch
        # if numbers[i+1].startswith(numbers[i]):
        #     ressult = 'NO'
        #     break

    print(result)