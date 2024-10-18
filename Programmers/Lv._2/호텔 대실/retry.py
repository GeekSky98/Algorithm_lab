def solution(book_time):
    start_list = sorted([int(i.split(':')[0]) * 60 + int(i.split(':')[1]) for i, _ in book_time])
    end_list = sorted([int(i.split(':')[0]) * 60 + int(i.split(':')[1]) + 10 for _, i in book_time])

    current_room = 0
    max_room = 0
    start_idx = 0
    end_idx = 0

    while start_idx < len(book_time):
        if start_list[start_idx] < end_list[end_idx]:
            start_idx += 1
            current_room += 1
            max_room = max(max_room, current_room)
        else:
            end_idx += 1
            current_room -= 1

    return max_room