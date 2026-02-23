import sys

input = sys.stdin.readline
print = sys.stdout.write

def mergesort(arr, left, right, temp):
    if right - left < 1:
        return

    m = (left + right) // 2
    
    mergesort(arr, left, m, temp)
    mergesort(arr, m + 1, right, temp)
    
    idx = left
    idx1 = left
    idx2 = m + 1

    while idx1 <= m and idx2 <= right:
        if  arr[idx1] < arr[idx2]:
            temp[idx] = arr[idx1]
            idx1 += 1
        elif arr[idx2] < arr[idx1]:
            temp[idx] = arr[idx2]
            idx2 += 1
        idx += 1
    
    while idx1 <= m:
        temp[idx] = arr[idx1]
        idx += 1
        idx1 += 1

    while idx2 <= right:
        temp[idx] = arr[idx2]
        idx += 1
        idx2 += 1

    for i in range(left, right + 1):
        arr[i] = temp[i]

N = int(input())
num = []
temp = [0] * N

for _ in range(N):
    num.append(int(input()))

mergesort(num, 0, N-1, temp)
for i in num:
    print(str(i) + '\n')