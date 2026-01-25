import sys

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
hap = [0]
hap[0] = num[0]
for i in range(1, n):
    hap.append(hap[i-1] + num[i])
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    if i == 1:
        sys.stdout.write(f"{str(hap[j-1])}\n")
    else:
        sys.stdout.write(f"{str(hap[j-1] - hap[i-2])}\n")