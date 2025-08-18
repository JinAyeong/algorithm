stars = [1.20, 2.19, 3.21, 4.20, 5.21, 6.22, 7.23, 8.23, 9.23, 10.23, 11.23, 12.22]
stars_used = [False] * 12

for _ in range(7):
    mon, day = input().split()
    if len(day) == 1:
        day = '0' + day

    str_date = float('.'.join([mon, day]))
    date = float(str_date)

    for i in range(12):
        if i == 11:
            stars_used[11] = True
        elif stars[i] <= date < stars[i+1]:
            stars_used[i] = True
            break

all_failed = True
N = int(input())
passed = []

for _ in range(N):
    mon, day = input().split()
    if len(day) == 1:
        new_day = '0' + day
    else:
        new_day = day

    str_date = float('.'.join([mon, new_day]))
    date = float(str_date)

    for i in range(12):
        if i == 11:
            if not stars_used[11]:
                all_failed = False
                passed.append((int(mon), int(day)))
        elif stars[i] <= date < stars[i+1]:
            if not stars_used[i]:
                all_failed = False
                passed.append((int(mon), int(day)))
            break

passed.sort()

if all_failed:
    print('ALL FAILED')
else:
    for mon, day in passed:
        print(mon, day)