N, K = map(int, input().split())
classrooms = [0] + sorted(map(int, input().split()))
classrooms_dist = sorted(classrooms[i+1] - classrooms[i] for i in range(N))

print(sum(classrooms_dist[:N-K]))