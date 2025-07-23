k = int(input())
arr = list(input().split())
min_answer = '9999999999'
max_answer = '0'
used = [False] * 10

def dfs(i, string):
    global min_answer, max_answer

    if i == k + 1:
        min_answer = (string if int(min_answer) > int(string) else min_answer)
        max_answer = (string if int(max_answer) < int(string) else max_answer)
        return
    
    cur_dir = arr[i-1]
        
    for j in range(10):

        if used[j]:
            continue

        if (i == 0) or (cur_dir == '<' and int(string[-1]) < j) or (cur_dir == '>' and int(string[-1]) > j):
            used[j] = True
            dfs(i+1, string + str(j))
            used[j] = False

dfs(0, '')

print(max_answer)
print(min_answer)