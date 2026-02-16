import sys

input = sys.stdin.readline
print = sys.stdout.write

def mergesort(arr, left, right, temp):
    if right - left < 1:
        return 0
    
    m = (left + right) // 2

    result = mergesort(arr, left, m, temp)
    result += mergesort(arr, m + 1, right, temp)
    
    idx = left
    idx1 = left
    idx2 = m + 1

    while idx1 <= m and idx2 <= right:
        if arr[idx1] <= arr[idx2]:
            temp[idx] = arr[idx1]
            idx1 += 1
        elif arr[idx2] < arr[idx1]:
            temp[idx] = arr[idx2]
            result += m - idx1 + 1
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

    return result
    
N = int(input())
num = list(map(int, input().split()))
temp = [0] * N

result = mergesort(num, 0, N-1, temp)
print(str(result))