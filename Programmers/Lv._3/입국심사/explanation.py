def solution(n, times):
    left, right = 1, max(times) * n

    while left < right:
        mid = (left + right) // 2
        mid_time = sum(mid // server for server in times)

        if mid_time < n:
            left = mid + 1
        else:
            right = mid

    return left