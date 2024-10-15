def solution(s):
    answer = 0
    index = 0
    while index < len(s):
        target = s[index]
        count = 0
        other_count = 0

        while index < len(s):
            if s[index] == target:
                count += 1
            else:
                other_count += 1

            index += 1

            if count == other_count:
                break

        answer += 1

    return answer

print(solution("aaabbaccccabba"))