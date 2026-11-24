N, M, L = map(int, input().split()) # 현재 휴게소 수, 필요한 휴게소 수, 고속도로 길이
if N == 0:
    pos = []
else:
    pos = list(map(int, input().split()))

pos.sort()
print(pos)