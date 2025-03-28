from typing import List

# 브루트포스
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n

        for i in range(n):
            for j in range(i+1, n):
                if temperatures[i] < temperatures[j]:
                    answer[i] = j - i
                    break

        return answer