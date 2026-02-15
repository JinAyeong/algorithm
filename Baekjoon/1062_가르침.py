N, K = map(int, input().split())
words = [input() for _ in range(N)]

char = {'a', 'n', 't', 'i', 'c'}

for word in words:
    word_set = set(word)
    new = word_set.difference(char)
    print(new)