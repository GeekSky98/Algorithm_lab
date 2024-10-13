from collections import deque, defaultdict

s, p = map(int, input().split())
dna = input().strip()
A, C, G, T = list(map(int, input().split()))

dic = defaultdict(int)
cnt = 0
string = deque()

for i in range(p):
    value = dna[i]
    string.append(value)
    dic[value] += 1

if dic['A'] >= A and dic['C'] >= C and dic['G'] >= G and dic['T'] >= T:
    cnt += 1

for i in range(p, s):
    dic[string.popleft()] -= 1
    string.append(dna[i])
    dic[dna[i]] += 1
    if dic['A'] >= A and dic['C'] >= C and dic['G'] >= G and dic['T'] >= T:
        cnt += 1

print(cnt)