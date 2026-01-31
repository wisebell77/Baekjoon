import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
mat = list(map(int, sys.stdin.readline().split()))
start_index = 0
end_index = len(mat) - 1
count = 0

mat.sort()

while start_index < end_index:
    sum = mat[start_index] + mat[end_index]
    if sum == M:
        count += 1
        start_index += 1
        end_index -= 1
    elif sum < M:
        start_index += 1
    else:
        end_index -= 1

print(count)