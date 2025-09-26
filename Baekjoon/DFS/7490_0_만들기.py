def dfs(i, num, numbers, arr):

    if i == num-1:
        join_arr = "".join(arr)
        if eval(join_arr.replace(" ", "")) == 0:
            print(join_arr)
        return
    
    dfs(i+1, num, numbers, arr+[" "]+[str(numbers[i+1])])
    dfs(i+1, num, numbers, arr+['+']+[str(numbers[i+1])])
    dfs(i+1, num, numbers, arr+["-"]+[str(numbers[i+1])])


def solve(num):

    numbers = list(range(1, num+1))

    dfs(0, num, numbers, [str(numbers[0])])

for _ in range(int(input())):
    N = int(input())
    solve(N)
    print()