def solution(players, callings):
    rank = {j: i for i, j in enumerate(players)}

    for c in callings:
        idx = rank[c]
        players[idx], players[idx - 1] = players[idx - 1], players[idx]

        target = players[idx]

        rank[c] -= 1
        rank[target] += 1

    return players