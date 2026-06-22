from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):

    mp = [[0] * 102 for _ in range(102)]

    # 좌표 2배 확장 -> 사각형 채우기
    # (모서리 또는 꼭짓점만 맞닿는 경우 구분)
    for x1, y1, x2, y2 in rectangle:

        for x in range(x1 * 2, x2 * 2 + 1):
            for y in range(y1 * 2, y2 * 2 + 1):
                mp[x][y] = 1

    # 내부 제거
    for x1, y1, x2, y2 in rectangle:

        for x in range(x1 * 2 + 1, x2 * 2):
            for y in range(y1 * 2 + 1, y2 * 2):
                mp[x][y] = 0

    characterX, characterY = characterX * 2, characterY * 2
    itemX, itemY = itemX * 2, itemY * 2

    q = deque([(characterX, characterY, 0)])
    visited = [[False] * 102 for _ in range(102)]
    visited[characterX][characterY] = True

    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        x, y, dist = q.popleft()

        if x == itemX and y == itemY:
            return dist // 2

        for dx, dy in dir:
            nx, ny = x + dx, y + dy

            if (
                0 <= nx < 102 and
                0 <= ny < 102 and
                not visited[nx][ny] and
                mp[nx][ny] == 1
            ):
                visited[nx][ny] = True
                q.append((nx, ny, dist + 1))

    return 0