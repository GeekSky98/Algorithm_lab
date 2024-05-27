def solution(n, cores):
    if n <= len(cores):
        return n

    n -= len(cores)
    left, right = 0, max(cores) * n

    while left < right:
        mid = (left + right) // 2
        processed = sum(mid // core for core in cores)

        if processed < n:
            left = mid + 1
        else:
            right = mid

    t = left
    processed = sum((t - 1) // core for core in cores)
    n -= processed

    for i, core in enumerate(cores):
        if t % core == 0:
            n -= 1
            if n == 0:
                return i + 1