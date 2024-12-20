# L <= x <= R 이고, 8이 가장 적게 들어있는 수 x의 8의 개수

L, R = map(int, input().split())
str_L, str_R = str(L), str(R)
str_L = (len(str_R) - len(str_L)) * '0' + str_L

min_cnt = 0

if str_L == str_R:
    min_cnt += str_L.count('8')

else:

    # 첫 자리수가 둘 다 8이면 최소 1개 들어감
    for i in range(len(str_L)):

        if str_L[i] == str_R[i] == '8':
            min_cnt += 1

        elif str_L[i] == str_R[i]:
            continue

        else:
            break


print(min_cnt)