def solution(dirs):
    dir_dic = {'U':(0,1), 'D':(0,-1), 'R':(1,0), 'L':(-1,0)}
    visit_route = []
    x = y = 0
    for dir in list(dirs):
        xs, ys = dir_dic[dir]
        dx, dy = x+xs, y+ys
        route, route_reverse = (x, y, dx, dy), (dx, dy, x, y)
        if -5 <= dx <= 5 and -5 <= dy <= 5:
            x, y = dx, dy
            if route not in visit_route and route_reverse not in visit_route:
                visit_route.append(route)
    return len(visit_route)