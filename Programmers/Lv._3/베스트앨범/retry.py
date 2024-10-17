from collections import defaultdict
def solution(genres, plays):
    music_dic = defaultdict(list)
    cnt_dic = defaultdict(int)
    for i, genre in enumerate(genres):
        music_dic[genre].append((i, plays[i]))
        cnt_dic[genre] += plays[i]

    answer = []
    for key, _ in sorted(cnt_dic.items(), key=lambda x: -x[1]):
        for index, _ in sorted(music_dic[key], key=lambda x: (-x[1], x[0]))[:2]:
            answer.append(index)

    return answer