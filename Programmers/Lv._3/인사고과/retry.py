def solution(scores):
    a, b = scores[0]
    my_score = a + b
    scores.sort(key=lambda x: (-x[0], x[1]))
    rank = 1
    last_value = 0
    for x, y in scores:
        if y < last_value:
            if (x, y) == (a, b):
                return -1
            continue
        if x + y > my_score:
            rank += 1
        last_value = y
    return rank