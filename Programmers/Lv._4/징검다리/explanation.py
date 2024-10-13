def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)

    left, right = 0, distance
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        current = 0
        removed_rocks = 0
        min_dist = float('inf')

        for rock in rocks:
            diff_dist = rock - current
            if diff_dist < mid:
                removed_rocks += 1
            else:
                min_dist = min(min_dist, diff_dist)
                current = rock

        if removed_rocks > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1

    return answer