import sys

input = sys.stdin.readline
n, m = map(int, input().split())
A = [int(x) % m for x in input().split()]
hap = []
value = {}
temp = 0
cnt = 0

for i in A:
    temp = temp + i
    hap.append(temp)

for i in range(m):
    value[i] = 0

for i in range(len(hap)):
    hap[i] = hap[i] % m
    value[hap[i]] += 1

cnt = cnt + value[0]

for i in value.keys():
    if value[i] >= 2:
        cnt = cnt + (value[i] * (value[i]-1)) / 2

sys.stdout.write(str(int(cnt)))