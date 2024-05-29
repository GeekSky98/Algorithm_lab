def solution(gems):
    type_num = len(set(gems))
    left = right = 0
    gem_cnt = {}
    gem_cnt[gems[0]] = 1
    current_type = 1
    answer = [1, len(gems)]

    while left <= right < len(gems):
        if current_type == type_num:
            if right - left < answer[1] - answer[0]:
                answer = [left+1, right+1]

            gem_cnt[gems[left]] -= 1
            if gem_cnt[gems[left]] == 0:
                current_type -= 1
            left += 1
        else:
            right += 1
            if right < len(gems):
                if gems[right] in gem_cnt:
                    gem_cnt[gems[right]] += 1
                else:
                    gem_cnt[gems[right]] = 1
                if gem_cnt[gems[right]] == 1:
                    current_type += 1
    return answer