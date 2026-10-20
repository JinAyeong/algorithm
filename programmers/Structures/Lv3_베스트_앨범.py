from heapq import heappop, heappush, heapify


def solution(genres, plays):
    answer = []
    N = len(genres)
    
    genres_count = {}  # 총 재생 횟수
    genres_heap = {}   # 장르별 노래 재생 횟수 정렬
    
    for i in range(N):
        genre = genres[i]
        play_count = plays[i]
        
        if genre in genres_count:
            genres_count[genre] += play_count
        else:
            genres_count[genre] = play_count
        
        if genre in genres_heap:
            heappush(genres_heap[genre], (-play_count, i))
        else:
            genres_heap[genre] = [(-play_count, i)]
            heapify(genres_heap[genre])
            
    
    # 총 재생 정렬
    sorted_genres = sorted(genres_count.keys(), key=lambda x: genres_count[x], reverse=True)
    
    # 노래 뽑기
    for genre in sorted_genres:
        if genre in genres_heap:
            for _ in range(2):
                if genres_heap[genre]:
                    _, idx = heappop(genres_heap[genre])
                    answer.append(idx)
                else:
                    break
    
    return answer
