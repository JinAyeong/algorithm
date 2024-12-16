N = int(input())
words = [input().strip() for _ in range(N)]
words.sort()  # 사전순 정렬

result = 1


for i in range(1, N):

    if not words[i].startswith(words[i-1]):
        result += 1

print(result)