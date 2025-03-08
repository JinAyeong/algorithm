def solution(players, m, k):
    answer = 0
    server = [0] * 24 # 열린 서버 현황

    for p in range(24):

        # 서버 1개 이상 필요하다면, 현재 (필요한 서버 수 - 열린 서버) 만큼 증설
        if 1 <= players[p] // m:
            plus = players[p] // m

            if 0 < plus - server[p]:
                need = plus - server[p]
                answer += need

                for i in range(p, p + k):
                    if i < 24:
                        server[i] += need

    print(server)

    return answer