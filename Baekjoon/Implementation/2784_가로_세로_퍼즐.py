from itertools import permutations

words = sorted(input() for _ in range(6))

def can_puzzle(arr):

    words_arr = list(arr)

    for i in range(3):
        words_arr.append(arr[0][i] + arr[1][i] + arr[2][i])

    if sorted(words_arr) == words:
        return True
    return False


for puzzle in permutations(words, 3):

    if can_puzzle(puzzle):
        for line in puzzle:
            print(line)
        exit(0)

print(0)