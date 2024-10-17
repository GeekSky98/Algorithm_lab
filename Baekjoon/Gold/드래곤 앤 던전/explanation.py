from math import ceil

n, h = map(int, input().split())
rooms = [list(map(int, input().split())) for _ in range(n)]

left, right = 1,  10**18

answer = 0
while left <= right:
    mid = (left + right) // 2
    attack = h
    hp = mid
    for i, m_a, m_h in rooms:
        if i == 1:
            turn = ceil(m_h / attack)
            m_turn = ceil(hp / m_a)
            if m_turn < turn:
                hp = -1
                break
            else:
                hp -= m_a * (turn-1)
        else:
            attack += m_a
            hp = min(hp + m_h, mid)

    if hp <= 0:
        left = mid + 1
    else:
        answer = mid
        right = mid - 1

print(answer)


