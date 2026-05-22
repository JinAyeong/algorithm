from heapq import heappop, heapify

def solution(book_time):
    answer = 1
    
    def format_minute(original_time):
        original_h, original_m = original_time.split(':')
        
        return int(original_h) * 60 + int(original_m)
    
    book_time = list(map(lambda x: [format_minute(x[0]), format_minute(x[1])], book_time))
    heapify(book_time)
    
    room = [heappop(book_time)[1] + 10]
    
    while book_time:
        start, end = heappop(book_time)
        inserted = False
        
        for r, r_time in enumerate(room):
            if r_time <= start:
                room[r] = end + 10
                inserted = True
                break
                
        if not inserted:
            room.append(end + 10)
            answer += 1
        
    return answer# from heapq import heappop, heapify

# def solution(book_time):
#     answer = 1
    
#     def format_minute(original_time):
#         original_h, original_m = original_time.split(':')
        
#         return int(original_h) * 60 + int(original_m)
    
#     book_time = list(map(lambda x: [format_minute(x[0]), format_minute(x[1])], book_time))
#     heapify(book_time)
    
#     room = [heappop(book_time)[1] + 10]
    
#     while book_time:
#         start, end = heappop(book_time)
#         inserted = False
        
#         for r, r_time in enumerate(room):
#             if r_time <= start:
#                 room[r] = end + 10
#                 inserted = True
#                 break
                
#         if not inserted:
#             room.append(end + 10)
#             answer += 1
        
#     return answer

from heapq import heappush, heappop

def solution(book_time):

    def format_minute(t):
        h, m = map(int, t.split(':'))
        return h * 60 + m

    # 시작 시간 기준 정렬
    book_time = sorted([
        [format_minute(s), format_minute(e)]
        for s, e in book_time
    ])

    room = []

    for start, end in book_time:

        # 가장 빨리 비는 방 확인
        if room and room[0] <= start:
            heappop(room)

        # 현재 예약 넣기
        heappush(room, end + 10)

    return len(room)