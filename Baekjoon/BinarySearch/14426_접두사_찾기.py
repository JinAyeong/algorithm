for tc in range(int(input())):

    N, M = map(int, input().split())  # A수, B수
    A = sorted(map(int, input().split()))
    B = sorted(map(int, input().split()))

    result = 0
    last_result = M-1

    # 거꾸로 탐색하면서 숫자 지날 때마다 이분탐색 범위 조정
    for a in range(N-1, -1, -1):

        low, high = 0, last_result
        cur_a = A[a]
        cur_result = 0

        while low <= high:

            mid = (low + high) // 2
            cur_b = B[mid]

            # 현재 먹이 먹을 수 있으면 결과 갱신하고 더 높은 값 탐색
            if cur_a > cur_b:
                low = mid + 1
                cur_result = mid + 1
            # 현재 먹이 먹을 수 없으면 더 낮은 값 탐색
            else:
                high = mid - 1

        result += cur_result
        last_result = cur_result - 1

    print(result)