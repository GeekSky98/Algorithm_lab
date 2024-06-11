n = int(input())
def total_number(num, length):
    if length > 10:
        return
    result_list.append(num)
    for alpha in range(0, num % 10):
        total_number(num * 10 + alpha, length + 1)

result_list = []
for i in range(10):
    total_number(i, 1)

result_list.sort()

if n < len(result_list):
    print(result_list[n])
else:
    print(-1)