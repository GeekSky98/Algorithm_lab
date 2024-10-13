string = input().strip()

stack = []
str_flag = True
full_str = ""
for i in string:
    if i == "<":
        str_flag = False
        if stack:
            while stack:
                full_str += stack.pop()
        full_str += i
    elif i == ">":
        str_flag = True
        full_str += i
    elif str_flag:
        if i == " ":
            while stack:
                full_str += stack.pop()
            full_str += i
        else:
            stack.append(i)
    else:
        full_str += i

while stack:
    full_str += stack.pop()

print(full_str)