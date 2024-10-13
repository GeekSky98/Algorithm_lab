def solution_fail(s):
    s_len = len(s)
    max_len = 1

    if s_len % 2 == 1:
        for i in range(1, s_len):
            max_spread = min(i, s_len-i-1)
            for j in range(1, max_spread + 1):
                if s[i-j] == s[i+j]:
                    max_len = max(max_len, 2*j+1)
                else:
                    break
    else:
        for i in range(s_len-1):
            if s[i] == s[i+1]:
                max_len = max(max_len, s_len-i-2)
                max_spread = min(i, s_len-i-2)
                for j in range(1, max_spread + 1):
                    if s[i-j] == s[i+1+j]:
                        max_len = max(max_len, 2*j+2)
                    else:
                        break
            else:
                if i == 0:
                    max_len = max(max_len, 1)
                else:
                    max_spread = min(i, s_len - i - 1)
                    for j in range(1, max_spread + 1):
                        if s[i - j] == s[i + j]:
                            max_len = max(max_len, 2 * j + 1)
                        else:
                            break

    return max_len

# 중심 확장법 하다 보니 재밌어서 구현했지만 이상함.

def spread_detect(data, left, right, length):
    while left >= 0 and right < length and data[left] == data[right]:
        left -= 1
        right += 1
    return right - left - 1

def solution(s):
    max_len = 1
    s_len = len(s)
    for i in range(s_len):
        max_len = max(max_len, spread_detect(s, i, i, s_len), spread_detect(s, i, i + 1, s_len))
    return max_len

solution("abacde")