# K - (K & ((~K) + 1))  # 가장 오른쪽의 1만 삭제
#
# ex. K = 10110
# 1. (~K) = 01001
# 2. (~K) + 1 = 01010
# 3. K & ((~K) + 1) = 00010
# 4. K - (K & ((~K) + 1) = 10100 (가장 오른쪽의 1 사라짐)
#
# -> 이 연산 K가 0이 될 때까지 반복하면 1의 개수만큼 연산 시행


N = int(input())
K = input()
print(K.count("1"))