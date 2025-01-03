# python 32544KB 3020ms, pypy 111496KB 1516ms
# 1~N 사이의 숫자로 바꾸기, K자리수, 최대 P개의 LED 반전, 실제 X층에 서있음
# 각 LED 번호 비트로 변환
# 각 자릿수 순회하면서 바꿔야하는 LED 수 구하고, P개 이하이면서 N이하의 수일 경우에 += 1

LED = {
    "0": 0b1110111,
    "1": 0b0010010,
    "2": 0b1011101,
    "3": 0b1011011,
    "4": 0b0111010,
    "5": 0b1101011,
    "6": 0b1101111,
    "7": 0b1010010,
    "8": 0b1111111,
    "9": 0b1111011
}

N, K, P, X = map(int, input().split())

result = 0
current = '0' * (K - len(str(X))) + str(X)

for i in range(1, N+1):
    floor = '0' * (K - len(str(i))) + str(i)
    total_change = 0

    if i == X:
        continue

    for j in range(K):
        change = bin(LED[floor[j]] ^ LED[current[j]]).count('1')
        total_change += change

        if total_change > P:
            break

    if total_change <= P:
        result += 1

print(result)



#-----------------------------------------------------------------------
# 실패 코드
# 비트를 문자열로 표현해서 연산이 더 오래걸림 (python 시간초과, pypy 2068ms)

LED = {
    "0": '1110111',
    "1": '0010010',
    "2": '1011101',
    "3": '1011011',
    "4": '0111010',
    "5": '1101011',
    "6": '1101111',
    "7": '1010010',
    "8": '1111111',
    "9": '1111011'
}

N, K, P, X = map(int, input().split())

result = 0

for i in range(1, N+1):
    floor = '0' * (K - len(str(i))) + str(i)
    current = '0' * (K - len(str(X))) + str(X)
    total_change = 0

    if i == X:
        continue

    for j in range(K):
        change = format(int(LED[floor[j]], 2) ^ int(LED[current[j]], 2), '07b').count("1")
        total_change += change

        if total_change > P:
            break

    if total_change <= P:
        result += 1

print(result)