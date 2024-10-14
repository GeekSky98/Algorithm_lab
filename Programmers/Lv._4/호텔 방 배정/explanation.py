import sys
sys.setrecursionlimit(10 ** 8)

def solution(k, room_number):
    answer = []
    room_dic = {}

    def find_room(room):
        if room not in room_dic:
            room_dic[room] = room + 1
            return room

        next_room = find_room(room_dic[room])
        room_dic[room] = next_room + 1

        return next_room

    for i in room_number:
        answer.append(find_room(i))

    return answer



def solution(k, room_number):
    answer = []
    room_dic = {}

    def find_room(room):
        path = []
        while room in room_dic:
            path.append(room)
            room = room_dic[room]

        for r in path:
            room_dic[r] = room + 1

        room_dic[room] = room + 1
        return room

    for i in room_number:
        answer.append(find_room(i))

    return answer

