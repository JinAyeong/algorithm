def solution(players, callings):
    rank = {player: i for i, player in enumerate(players)}

    for name in callings:
        cur_idx = rank[name]  # 현재 위치
        front_idx = cur_idx - 1  # 바로 앞 선수의 위치
        front_player = players[front_idx]

        # 두 선수 위치 교환
        players[front_idx], players[cur_idx] = players[cur_idx], players[front_idx]

        # 등수 정보 갱신
        rank[name] = front_idx
        rank[front_player] = cur_idx

    return players