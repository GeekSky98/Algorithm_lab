def solution(book_time):
    book_time = [(int(start.split(':')[0]) * 60 + int(start.split(':')[1]), int(end.split(':')[0]) * 60 + int(end.split(':')[1]) + 10) for start, end in book_time]
    starts, ends, book_len = sorted([book[0] for book in book_time]), sorted([book[1] for book in book_time]), len(book_time)
    room_cnt = max_room = start_idx = end_idx = 0
    while start_idx < book_len:
        if starts[start_idx] < ends[end_idx]:
            room_cnt += 1
            max_room = max(room_cnt, max_room)
            start_idx += 1
        else:
            room_cnt -= 1
            end_idx += 1
    return max_room