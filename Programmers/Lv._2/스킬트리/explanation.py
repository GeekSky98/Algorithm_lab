def solution(skill, skill_trees):
    answer = 0
    skill = list(skill)
    for skill_tree in skill_trees:
        prime = [s for s in skill_tree if s in skill]
        if prime == skill[:len(prime)]:
            answer += 1

    return answer

solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])