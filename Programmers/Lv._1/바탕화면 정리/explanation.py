def solution(wallpaper):
    u = l = float('inf')
    d = r = -float('inf')

    for x, line in enumerate(wallpaper):
        for y, v in enumerate(line):
            if v == '#':
                u = min(u, x)
                d = max(d, x)
                l = min(l, y)
                r = max(r, y)

    d += 1
    r += 1

    return [u, l, d, r]