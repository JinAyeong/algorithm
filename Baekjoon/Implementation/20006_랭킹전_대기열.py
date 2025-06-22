'''
매칭 가능한 방 : 처음 입장한 플레이어의 레벨 += 10
입장 가능한 방 없으면 새로운 방 생성
입장 가능한 방 여러개면 가장 먼저 생성된 방 입장
정원 다 찼으면 Started! 출력
'''

p, m = map(int, input().split())
rooms = []

for _ in range(p):
    joined = False
    l, n = map(str, input().split())

    for i in range(len(rooms)):
        level = rooms[i][0][0]
        if len(rooms[i]) < m and level - 10 <= int(l) <= level + 10:
            rooms[i].append([int(l), n])
            joined = True
            break

    if not joined:
        rooms.append([[int(l), n]])

for room in rooms:

    print('Started!' if len(room) == m else 'Waiting!')

    for member in sorted(room, key=lambda x: x[1]):
        print(*member)