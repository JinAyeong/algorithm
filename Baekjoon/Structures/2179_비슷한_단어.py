'''
반례
6
bc
aa
ab
ba
bd
bb
'''

N = int(input())
words = [input() for _ in range(N)]
sorted_words = [(word, index) for index, word in enumerate(words)]
sorted_words.sort(key=lambda x:x[0])

max_l = 0

result = [float('inf'), float('inf')]

for i in range(N-1):

    word1, idx1 = sorted_words[i]

    for j in range(i+1, N):
        word2, idx2 = sorted_words[j]

        if word1 == word2:
            continue

        cur_l = 0

        for k in range(min(len(word1), len(word2))):
            if word1[k] == word2[k]:
                cur_l += 1
            else:
                break

        if cur_l > max_l:
            max_l = cur_l
            result = [idx1, idx2]

        elif cur_l == max_l:
            if min(idx1, idx2) < min(result):
                result = [idx1, idx2]
            elif min(idx1, idx2) == min(result):
                if max(idx1, idx2) < max(result):
                    result = [idx1, idx2]

        else:
            break

result.sort()

print(words[result[0]])
print(words[result[1]])