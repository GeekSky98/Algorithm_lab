def solution(babbling):
    answer = 0
    for word in babbling:
        for i in ["aya", "ye", "woo", "ma"]:
            word = word.replace(i, " ")
        if not word.strip():
            answer += 1

    return answer