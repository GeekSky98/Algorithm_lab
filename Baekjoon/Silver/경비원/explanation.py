n, m = map(int, input().split())
store_num = int(input())
store_list = [tuple(map(int, input().split())) for _ in range(store_num)]
my_location = tuple(map(int, input().split()))

total_dist = 2*n + 2*m
def distance(d, num):
    if d == 1:
        return num
    elif d == 2:
        return n + m + (n - num)
    elif d == 3:
        return (2 * n) + m + (m - num)
    else:
        return n + num

store_location = []
for d, num in store_list:
    store_location.append(distance(d, num))

dong = distance(my_location[0], my_location[1])

answer = 0
for s in store_location:
    if dong > s:
        dist = (total_dist + s) - dong
    else:
        dist = s - dong

    if dong > s:
        dist_reverse = dong - s
    else:
        dist_reverse = total_dist - (s - dong)

    answer += min(dist, dist_reverse)

print(answer)