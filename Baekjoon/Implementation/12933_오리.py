sound = list(input())
mp = {
    'q': 0,
    'u': 1,
    'a': 2,
    'c': 3,
    'k': 4
}
cnt = [0, 0, 0, 0, 0]

answer = 0

for char in sound:
    idx = mp[char]

    if idx == 0:
        cnt[0] += 1

    elif idx != 0:
        if cnt[idx-1] > cnt[idx]:
            cnt[idx] += 1
        else:
            answer = -1
            break

    if idx == 4:
        cnt = list(map(lambda x: x-1, cnt))

    answer = max(answer, cnt[0])

if any(cnt):
    answer = -1

print(answer)