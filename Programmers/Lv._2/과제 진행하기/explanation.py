def solution(plans):
    plan_len = len(plans)
    answer = []
    least_sub = []

    plans = list(map(lambda x: [int(x[1].split(":")[0])*60 + int(x[1].split(":")[1]), int(x[2]), x[0]], plans))
    plans.sort(key=lambda x: x[0])

    for i, sub in enumerate(plans):
        if i < plan_len-1:
            total, next_time, subject = sub[0] + sub[1], plans[i+1][0], sub[2]
            if total <= next_time:
                answer.append(subject)
                diff = next_time - total
                while least_sub and diff>0:
                    if least_sub[-1][0] > diff:
                        least_sub[-1][0] -= diff
                        break
                    else:
                        answer.append(least_sub[-1][1])
                        diff -= least_sub.pop(-1)[0]
            else:
                least_sub.append([total-next_time, subject])
        else:
            answer.append(sub[2])
    while least_sub:
        answer.append(least_sub.pop(-1)[1])

    return answer