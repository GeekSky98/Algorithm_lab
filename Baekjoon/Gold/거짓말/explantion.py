import sys
n, m = map(int, sys.stdin.readline().split())
know_list = list(map(int, sys.stdin.readline().split()))
know_people = set(know_list[1:])
party = [set(list(map(int, sys.stdin.readline().split()))[1:]) for _ in range(m)]

for _ in range(m):
    for p in party:
        if p & know_people:
            know_people = know_people | p

party_cnt = 0
for p in party:
    if not p & know_people:
        party_cnt += 1

print(party_cnt)