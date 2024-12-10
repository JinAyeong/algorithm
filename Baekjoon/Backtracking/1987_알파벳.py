R, C = map(int, input().split())  # 세로, 가로
board = [list(input()) for _ in range(R)]
max_move = 0

def move(i, a, b, alpha):
    global max_move
    max_move = max(max_move, i)

    for k in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        na, nb = a + k[0], b + k[1]

        if 0 <= na < R and 0 <= nb < C and board[na][nb] not in alpha:
            alpha.add(board[na][nb])
            move(i + 1, na, nb, alpha)
            alpha.remove(board[na][nb])

move(1, 0, 0, {board[0][0]})

print(max_move)