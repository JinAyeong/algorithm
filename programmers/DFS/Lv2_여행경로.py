def solution(tickets):
    global answer

    tickets.sort(key=lambda x: (x[0], x[1]))
    answer = []

    def travel(lst):
        global answer

        if all(used):
            answer = lst
            return True

        for idx, ticket in enumerate(tickets):

            if lst[-1] == ticket[0] and not used[idx]:
                used[idx] = True
                if travel(lst + [ticket[1]]):
                    return True
                used[idx] = False

        return False

    used = [False] * len(tickets)

    for i, t in enumerate(tickets):

        used[i] = True
        if travel(t):
            return answer
        used[i] = False
