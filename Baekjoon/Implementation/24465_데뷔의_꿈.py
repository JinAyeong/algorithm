stars = [1.20, 2.19, 3.21, 4.20, 5.21, 6.22, 7.23, 8.23, 9.23, 10.23, 11.23, 12.22]
stars_used = [False] * 12

def to_float(mon: str, day: str) -> float:
    day = day.zfill(2)
    return float(f"{int(mon)}.{day}")

def star_index(date: float) -> int:
    for i in range(12):
        if i == 11 or stars[i] <= date < stars[i+1]:
            return i
    return -1

for _ in range(7):
    mon, day = input().split()
    idx = star_index(to_float(mon, day))
    stars_used[idx] = True

N = int(input())
candidates = []

for _ in range(N):
    mon, day = input().split()
    idx = star_index(to_float(mon, day))

    if not stars_used[idx]:
        candidates.append((int(mon), int(day)))

if not candidates:
    print("ALL FAILED")
else:
    for mon, day in sorted(candidates):
        print(mon, day)