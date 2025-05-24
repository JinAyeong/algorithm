'''
사진 게시 기준
1. 비어있는 사진틀에 먼저
2. 추천 횟수가 가장 적은 학생 삭제 -> 새로운 학생 추가
3. 마지막 추천이 가장 오래된 학생 삭제 -> 새로운 학생 추가
'''

n = int(input())
_ = int(input())
recommends = list(map(int, input().split()))

frame = []  # [{id: 학생번호, vote: 추천수, idx: 추천받은 순서}]

for idx, student in enumerate(recommends):

    # for ... else : for문이 break를 만나지 않고 정상적으로 끝났을 때만 else 블록 실행
    for f in frame:
        if f['id'] == student:
            f['vote'] += 1
            break
    else:
        if len(frame) >= n:
            # 추천 수 적고 오래된 순으로 제거
            frame.sort(key=lambda x: (x['vote'], x['idx']))
            frame.pop(0)
        frame.append({'id': student, 'vote': 1, 'idx': idx})


frame.sort(key=lambda x: x['id'])

for f in frame:
    print(f["id"], end=" ")