N, K = map(int, input().split()) # N개의 커피, K만큼의 카페인
coffees = list(map(int, input().split()))
coffees.sort()

dp = [0, 0] * (N+1)

