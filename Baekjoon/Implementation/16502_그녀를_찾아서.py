N = int(input())
M = int(input())
adjl = {'A': [], 'B': [], 'C': [], 'D': []}

for _ in range(M):
    S, E, prob = input().split()
    adjl[S].append((E, float(prob)))

cur_prob = {'A': 0.25, 'B': 0.25, 'C': 0.25, 'D': 0.25}

for _ in range(N):
    new_prob = {'A': 0.00, 'B': 0.00, 'C': 0.00, 'D': 0.00}

    for key, lst in adjl.items():
        for next, prob in lst:
            new_prob[next] += cur_prob[key] * prob

    cur_prob = new_prob

for pos in ['A', 'B', 'C', 'D']:
    print((cur_prob[pos]) * 100)