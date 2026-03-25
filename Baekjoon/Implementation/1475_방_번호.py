from collections import Counter

number_dict = Counter(map(int, list(input())))
number_dict[6] = number_dict[9] = (number_dict[6] + number_dict[9]) // 2 + (number_dict[6] + number_dict[9]) % 2

print(max(number_dict.values()))