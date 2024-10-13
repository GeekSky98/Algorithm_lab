def solution(elements):
    answer = set()
    e_len = len(elements)
    expand_list = elements + elements[:-1]
    for i in range(1, e_len + 1):
        for j in range(e_len):
            answer.add(sum(expand_list[j:j + i]))

    return len(answer)