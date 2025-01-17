# Y: 2 윷놀이, F: 3 같은 그림 찾기, O: 4 원카드
# 게임 최대 몇번 가능한지?

N, game = input().split()
players = set()
games = {'Y': 2, 'F': 3, 'O': 4}

for _ in range(int(N)):

    players.add(input())

print(len(players) // (games[game] - 1))