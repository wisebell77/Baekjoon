import sys

N = int(sys.stdin.readline())
A = []
max = 0

for i in range(N):
    a = int(sys.stdin.readline())
    A.append([a, i])


B = sorted(A)

for i in range(N):
    m = B[i][1] - i
    if m > max:
        max = m

print(max + 1)