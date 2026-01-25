import sys

n, m = map(int, sys.stdin.readline().split())
matrix = []
hap = []

for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

for _ in range(n+1):
    lst = []
    for _ in range(n+1):
        lst.append(0)
    hap.append(lst)

for i in range(1, n+1):
    for j in range(1, n+1):
        hap[i][j] = hap[i][j-1] + hap[i-1][j] - hap[i-1][j-1] + matrix[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    sys.stdout.write(f"{hap[x2][y2] - hap[x2][y1-1] - hap[x1-1][y2] + hap[x1-1][y1-1]}\n")