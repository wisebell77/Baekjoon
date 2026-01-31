import sys

N = int(sys.stdin.readline())
start_index = 1
end_index = 1
count = 0

while end_index <= N:
    if (start_index + end_index) * (end_index - start_index + 1) / 2 > N:
        start_index += 1
    if (start_index + end_index) * (end_index - start_index + 1) / 2 < N:
        end_index += 1
    if (start_index + end_index) * (end_index - start_index + 1) / 2 == N:
        count += 1
        end_index += 1

print(count)