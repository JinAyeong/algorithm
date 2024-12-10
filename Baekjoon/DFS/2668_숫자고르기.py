N = int(input())
arr = [int(input()) for _ in range(N)]
arr = [0] + arr

result_arr = []

def select(num, index_arr, num_arr):
    global result_arr

    if num in index_arr:

        if set(index_arr) == set(num_arr):
            result_arr = result_arr + index_arr
        
        return
    
    select(arr[num], index_arr + [num], num_arr + [arr[num]])


for i in range(1, N+1):

    if i in result_arr:
        continue
    
    select(arr[i], [i], [arr[i]])

result_arr = list(set(result_arr))
result_arr.sort()
print(len(result_arr))
for result in result_arr:
    print(result)