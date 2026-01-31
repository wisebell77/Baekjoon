import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
count = 0

num.sort()

for i in range(N):
    start_index = 0
    end_index = N - 1
    while start_index < end_index:
        sum = num[start_index] + num[end_index]
        if sum == num[i]:
            if start_index != i and end_index != i:
                count += 1
                break
            elif start_index == i:
                start_index += 1
            elif end_index == i:
                end_index -= 1
        elif sum < num[i]:
            start_index += 1
        else:
            end_index -= 1

print(count)