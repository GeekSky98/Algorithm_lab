import sys
n, t_n = map(int, sys.stdin.readline().split())
elev = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
test = [list(map(int, sys.stdin.readline().split())) for _ in range(t_n)]

for i in range(1, n):
    elev[i][0] += elev[i-1][0]
for i in range(1, t_n):
    test[i][0] += test[i-1][0]

answer = e_i = t_i = 0
while e_i < n:
    now_e, now_t = elev[e_i][0], test[t_i][0]
    e_limit, t_speed = elev[e_i][1], test[t_i][1]
    if now_e < now_t:
        e_i += 1
    elif now_e > now_t:
        t_i += 1
    else:
        e_i += 1
        t_i += 1
    if t_speed > e_limit:
        answer = max(answer, t_speed - e_limit)

print(answer)