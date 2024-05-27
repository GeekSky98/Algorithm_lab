def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    last_time = -30001
    camera_cnt = 0

    for r in routes:
        if r[0] > last_time:
            last_time = r[1]
            camera_cnt += 1

    return camera_cnt