N = int(input())
perm = [int(input()) for _ in range(N)]
pos = []
neg = []
zero = False

answer = 0

for num in perm:
    if num > 0:
        pos.append(num)
    elif num < 0:
        neg.append(num)
    elif num == 0:
        zero = True

pos.sort()
neg.sort()

'''
-12, -5, -1
'''

for i in range(len(pos)-1, -1, -2):
    if i == 0:
        answer += pos[i]
    else:
        answer += max(pos[i] * pos[i-1], pos[i] + pos[i-1])

for j in range(0, len(neg), 2):
    if j == len(neg)-1:
        if not zero:
            answer += neg[j]
        else:
            continue
    else:
        answer += max(neg[j] * neg[j+1], neg[j] + neg[j+1])

print(answer)