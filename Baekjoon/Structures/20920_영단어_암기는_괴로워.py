# 단어장 정렬 우선순위
# 1. 빈도수
# 2. 단어의 길이
# 3. 사전순

from collections import defaultdict

N, M = map(int, input().split()) # 단어 수, 외울 단어의 길이

word_dict = defaultdict(int)

# 단어세기
for _ in range(N):
    word = input()
    if len(word) >= M:
        word_dict[word] += 1

word_list = []

# 우선순위 순서대로 append
for word, cnt in word_dict.items():
    word_list.append((cnt, len(word), word))

# 정렬
word_list.sort(key=lambda x:(-x[0], -x[1], x[2]))

# 출력
for word in word_list:
    print(word[2])