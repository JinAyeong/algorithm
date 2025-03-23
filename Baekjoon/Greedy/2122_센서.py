N = int(input()) # 센서 수
K = int(input()) # 집중국 수
sensors = list(map(int, input().split()))
sensors.sort()

dist = [sensors[i] - sensors[i-1] for i in range(1, N)]
dist.sort()
print(sum(dist[:N-K]))