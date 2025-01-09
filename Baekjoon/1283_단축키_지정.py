N = int(input())
key = set()

def make_key(option):
    global key

    # 조건 1번으로 단축키 검사
    for j in range(len(option)):

        if option[j][0].lower() not in key:
            key.add(option[j][0].lower())
            option[j] = '[' + option[j][0] + ']' + option[j][1:]

            return option


    # 조건 2번으로 단축키 검사
    for k in range(len(option)):
        for l in range(1, len(option[k])):

            if option[k][l].lower() not in key:
                key.add(option[k][l].lower())
                option[k] = option[k][:l] + '[' + option[k][l] + ']' + option[k][l+1:]

                return option

    # 조건 1, 2 둘 다 단축키 못만들면 그대로 return
    return option


for i in range(N):

    option = list(input().split())
    print(*make_key(option))