data = input().strip()

cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for c in cro:
    data = data.replace(c, '#')

print(len(data))