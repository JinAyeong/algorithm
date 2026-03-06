'''
정렬 기준
1. 파일명 사전순
2. os 인식 확장자가 붙은 순
3. os 파일 확장자 사전순
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 파일 수, os 인식 확장자 수
files = [input().strip().split('.') for _ in range(N)]
os_extension = set(input().strip() for _ in range(M))

files.sort(key=lambda x: (x[0], 0 if (len(x) == 2 and x[1] in os_extension) else 1, x[1]))

for name, ext in files:
    print(f"{name}.{ext}")