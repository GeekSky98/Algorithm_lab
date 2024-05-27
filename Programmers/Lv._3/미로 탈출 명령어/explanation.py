import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def solution(n, m, x, y, r, c, k):
    manhattan = abs(x - r) + abs(y - c)
    if manhattan > k or (k - manhattan) % 2 == 1:
        return "impossible"

    best_routes = "z"
    direction = [(1, 0), (0, -1), (0, 1), (-1, 0)]
    index = ["d", "l", "r", "u"]

    def detect(dx, dy, cnt, path, limit):
        nonlocal best_routes
        if path > best_routes:
            return

        rm, dt = limit - cnt, abs(dx - r) + abs(dy - c)
        if dt > rm or (rm - dt) % 2 == 1:
            return

        if cnt == limit and (dx, dy) == (r, c):
            best_routes = path
            return

        for i, (j, k) in enumerate(direction):
            next_x, next_y = dx + j, dy + k
            if 1 <= next_x <= n and 1 <= next_y <= m:
                detect(next_x, next_y, cnt+1, path + index[i], limit)

    detect(x, y, 0, "", k)

    return best_routes