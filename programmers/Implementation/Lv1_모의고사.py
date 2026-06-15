def solution(answers):
    answer = []
    max_score = 0
    n = len(answers)
    
    number_1 = [1, 2, 3, 4, 5]
    number_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    number_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    number_1_score = sum(1 if number_1[i % 5] == answers[i] else 0 for i in range(n))
    number_2_score = sum(1 if number_2[i % 8] == answers[i] else 0 for i in range(n))
    number_3_score = sum(1 if number_3[i % 10] == answers[i] else 0 for i in range(n))
    
    scores = [number_1_score, number_2_score, number_3_score]
    max_score = max(scores)

    for i, score in enumerate(scores):
        if score == max_score:
            answer.append(i + 1)
    
    return answer