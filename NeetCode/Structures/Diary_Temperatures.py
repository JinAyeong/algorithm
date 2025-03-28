from typing import List

# 브루트포스
class Solution1:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n

        for i in range(n):
            for j in range(i+1, n):
                if temperatures[i] < temperatures[j]:
                    answer[i] = j - i
                    break

        return answer

# 스택
class Solution2:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []

        for i in range(n):
            while stack:
                if temperatures[i] > stack[-1][0]:
                    temperature, idx = stack.pop()
                    answer[idx] = i - idx

                else:
                    break

            stack.append((temperatures[i], i))

        return answer