string = input().split('-')
answer = []
for i in string:
    answer.append(sum(map(int, i.split('+'))))

if len(answer) == 1:
    print(answer[0])
else:
    value = answer[0]
    for i in range(1, len(answer)):
        value -= answer[i]
    print(value)