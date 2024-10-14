def solution(diffs, times, limit):
    p_len = len(diffs)

    def solve_puzzle(level):
        total_time = 0
        prev_time = 0

        for i in range(p_len):
            current = times[i]
            if level < diffs[i]:
                total_time += (diffs[i] - level) * (prev_time + current) + current
            else:
                total_time += current

            if total_time > limit:
                return False

            prev_time = current

        return True

    left, right = 1, max(diffs)

    while left < right:
        mid = (left + right) // 2

        if solve_puzzle(mid):
            right = mid
        else:
            left = mid + 1

    return left