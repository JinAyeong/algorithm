N = int(input())
drinks = sorted(map(int, input().split()))

answer = sum(drinks[i] / 2 for i in range(N-1))

print(answer + drinks[-1])