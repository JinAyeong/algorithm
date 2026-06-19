def solution(begin, target, words):
    if target not in words:
        return 0

    answer = float('inf')
    used = [False] * len(words)

    def dfs(depth, cur_word):
        nonlocal answer

        if depth >= answer:
            return

        if cur_word == target:
            answer = depth
            return

        for i, next_word in enumerate(words):
            if used[i]:
                continue

            diff_cnt = sum(a != b for a, b in zip(cur_word, next_word))

            if diff_cnt == 1:
                used[i] = True
                dfs(depth + 1, next_word)
                used[i] = False

    dfs(0, begin)

    return answer