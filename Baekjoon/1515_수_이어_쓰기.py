num = input()
N = 1
index = 0

while index < len(num):

    for n in range(len(str(N))):
        if str(N)[n] == num[index]:
            index += 1

            if index >= len(num):
                break

    N += 1

print(N-1)