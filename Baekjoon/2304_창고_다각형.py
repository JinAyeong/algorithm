# 현재보다 높은게 나오면 갱신
# 현재보다 낮은게 나오면

N = int(input())

stack = []
result = 0

storage = [list(map(int, input().split())) for _ in range(N)]
storage.sort()



print(result)