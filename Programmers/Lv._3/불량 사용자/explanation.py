import re
def solution(user_id, banned_id):
    answer_set = set()
    banned_regex = [re.compile("^" + b.replace("*", ".") + "$") for b in banned_id]

    def compare(user_list, ban_index, result):
        if len(banned_regex) == len(result):
            answer_set.add(frozenset(result))
            return

        for i, user in enumerate(user_list):
            if banned_regex[ban_index].match(user):
                compare(user_list[:i]+user_list[i+1:], ban_index+1, result+[user])

    compare(user_id, 0, [])
    return len(answer_set)