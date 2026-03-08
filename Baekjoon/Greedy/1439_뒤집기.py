S = input()
cal_map = {'0': 0, '1': 0}

for i in range(len(S)):
    if S[i-1] != S[i]:
        cal_map[S[i]] += 1

print(min(cal_map['0'], cal_map['1']))