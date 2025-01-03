str = input()
char = list(set(str))
char.sort() # 사전순 정렬

odd = 0
char_dic = {}

for c in char:

    c_count = str.count(c)
    char_dic[c] = c_count

    if c_count % 2 == 1:

        # 홀수개인 문자 두번째 나타났을 때 : 팰린드롬 실패
        if odd != 0:
            print("I'm Sorry Hansoo")
            exit(0)
        elif odd == 0:
            odd = c


answer = []

# 팰린드롬 만들기
for c in char:

    length = char_dic[c] // 2
    answer += [c] * length


if odd == 0:
    answer = answer + answer[::-1]
else:
    answer = answer + [odd] + answer[::-1]

print(''.join(answer))