def solution(land):
    width = len(land[0])
    height = len(land)
    detected = [[False for _ in range(width)] for _ in range(height)]
    result_dic = {}

    def detect(h, w):
        if land[h][w] == 0 or detected[h][w]:
            return 0, set()
        stack = [(h, w)]
        size = 0
        columns = set()
        while stack:
            h, w = stack.pop()
            if 0 <= h < height and 0 <= w < width and not detected[h][w] and land[h][w] == 1:
                detected[h][w] = True
                size += 1
                columns.add(w)
                for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    stack.append((h + i, w + j))
        return size, columns

    for w in range(width):
        for h in range(height):
            if land[h][w] == 1 and not detected[h][w]:
                size, columns = detect(h, w)
                for col in columns:
                    result_dic[col] = result_dic.get(col, 0) + size

    return max(result_dic.values())