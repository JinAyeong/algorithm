for _ in range(int(input())):

    W = input() # 알파벳
    N = len(W)
    K = int(input()) # 양의 정수
    alpha = list(set(W))

    # answer1: 어떤 문자를 K개 포함하는 가장 짧은 연속 문자열의 길이
    # answer2: 어떤 문자를 K개 포함하고, 문자열의 첫 글자와 마지막 글자가 해당문자인 가장 긴 연속 문자열의 길이
    answer_1 = float('inf')
    answer_2 = -1

    for a in alpha:
        
        idx = [i for i in range(N) if W[i] == a]

        if len(idx) < K:
            continue

        for j in range(N-K+1):
            length = idx[j+K-1] - idx[j]
            answer_1 = min(answer_1, length)
            answer_2 = max(answer_2, length)

    if answer_1 == float('inf') or answer_2 == -1:
        print(-1)
    else:
        print(answer_1, answer_2)