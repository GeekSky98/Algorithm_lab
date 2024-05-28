def solution(cards):
    def find_group_size(start, cards, visited):
        size = 0
        current = start
        while not visited[current]:
            visited[current] = True
            size += 1
            current = cards[current] - 1
        return size

    visited = [False] * len(cards)
    group_sizes = []

    for i in range(len(cards)):
        if not visited[i]:
            group_size = find_group_size(i, cards, visited)
            group_sizes.append(group_size)

    if len(group_sizes) < 2:
        return 0
    else:
        group_sizes.sort(reverse=True)
        return group_sizes[0] * group_sizes[1]