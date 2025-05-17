S, P = map(int, input().split())
dna = input()
A, C, G, T = map(int, input().split())

dna_cnt = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

def check(dict):

    if dict['A'] < A:
        return False
    if dict['C'] < C:
        return False
    if dict['G'] < G:
        return False
    if dict['T'] < T:
        return False
    return True

result = 0

for i in range(S):

    dna_cnt[dna[i]] += 1

    if i >= P:
        dna_cnt[dna[i-P]] -= 1

    if i >= P-1 and check(dna_cnt):
        result += 1

print(result)