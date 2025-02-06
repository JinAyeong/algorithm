A, B, C = map(int, input().split())

result = set()

def water(a, b, c):

    if a == 0:
        result.add(c)

