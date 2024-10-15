def solution(video_len, pos, op_start, op_end, commands):
    def time2int(string):
        h, m = string.split(':')
        return int(h) * 60 + int(m)

    v = time2int(video_len)
    p = time2int(pos)
    o_s = time2int(op_start)
    o_e = time2int(op_end)

    if o_s <= p < o_e:
        p = o_e

    for c in commands:
        if c == 'prev':
            p = max(0, p - 10)
        else:
            p = min(p + 10, v)

        if o_s <= p < o_e:
            p = o_e

    h, m = divmod(p, 60)
    return str(h).zfill(2) + ':' + str(m).zfill(2)

print(solution("10:55","00:05","00:15","06:55",["prev", "next", "next"]))