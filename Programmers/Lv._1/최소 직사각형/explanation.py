def solution(sizes):
    sizes = list(map(lambda x: sorted(x), sizes))
    max_x = max_y = 0
    for x, y in sizes:
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    return max_x * max_y