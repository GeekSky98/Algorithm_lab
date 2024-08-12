import sys
n = int(input())
num_list = [input() for _ in range(n)]

int_list = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000][::-1]
rome_list = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"][::-1]
rome_dic = {i:j for i,j in  zip(rome_list, int_list)}

def rome_to_int(data, dict):
    result = index = 0
    while index < len(data)-1:
        if dict[data[index]] < dict[data[index+1]]:
            result -= dict[data[index]]
        else:
            result += dict[data[index]]
        index += 1
    result += dict[data[-1]]

    return result

def int_to_rome(data, i_list, r_list):
    result = ""
    index = 0
    while data > 0:
        for _ in range(data // i_list[index]):
            data -= i_list[index]
            result += r_list[index]
        index += 1

    return result

for num in num_list:
    if num.isdigit():
        print(int_to_rome(int(num), int_list, rome_list))
    else:
        print(rome_to_int(num, rome_dic))