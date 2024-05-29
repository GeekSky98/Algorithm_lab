def solution(info, edge):
    answer = []
    visited_list = [0] * len(info)
    visited_list[0] = 1
    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return
        for parent, child in edge:
            if visited_list[parent] and not visited_list[child]:
                visited_list[child] = 1
                if info[child] == 0:
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                visited_list[child] = 0
    dfs(1, 0)
    return max(answer)