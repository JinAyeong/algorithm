'''
자카드 유사도 = 교집합 원소 수 / 합집합 원소 수
- a, b 공집합일 경우 자카드 유사도 = 1
- 다중집합 허용 가능
- 문자열일 경우 두 글자씩 끊어서 다중집합 생성
'''
from collections import Counter
from math import floor

def solution(str1, str2):
    
    l1, l2 = len(str1), len(str2)
    arr1 = [(str1[i] + str1[i+1]).lower() for i in range(l1-1) if (str1[i] + str1[i+1]).isalpha()]
    arr2 = [(str2[i] + str2[i+1]).lower() for i in range(l2-1) if (str2[i] + str2[i+1]).isalpha()]

    if not arr1 and not arr2: return 65536

    dict1 = Counter(arr1)
    dict2 = Counter(arr2)
    
    inter_set = set(arr1) & set(arr2)
    union_set = set(arr1) | set(arr2)
    
    inter_dict = {char: min(dict1[char], dict2[char]) for char in inter_set}
    union_dict = {char: max(dict1[char], dict2[char]) for char in union_set}
    
    intersection = sum(inter_dict.values())
    union = sum(union_dict.values())
    answer = floor((intersection/union) * 65536)
    
    return answer