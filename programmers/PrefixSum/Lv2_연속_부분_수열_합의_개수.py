def solution(elements):
    n = len(elements)
    circle_elements = elements + elements[:-1]

    m = len(circle_elements)
    prefix = [0] * (m + 1)

    for i in range(m):
        prefix[i + 1] = prefix[i] + circle_elements[i]

    answer = set(elements)

    for i in range(2, n + 1):
        for j in range(m - i + 1):
            answer.add(prefix[j + i] - prefix[j])

    return len(answer)