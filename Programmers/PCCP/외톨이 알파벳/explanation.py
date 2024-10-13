def solution(input_string):
    visit = set()
    answer = set()
    prev = None
    for i in (input_string):
        if i in visit:
            if i != prev:
                answer.add(i)
        else:
            visit.add(i)
        prev = i

    return "".join(sorted(list(answer))) if answer else "N"