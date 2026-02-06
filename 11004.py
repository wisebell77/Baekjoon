N, K = map(int, input().split())
A = list(map(int, input().split()))
K -= 1

def swap(L: list, start: int, end: int):
    L[start], L[end] = L[end], L[start]

def quicksort(L: list, start: int, end: int, K: int):
    pivot = L[(start + end)//2]
    left = start
    right = end
    while left <= right:
        while L[left] < pivot:
            left += 1
        while L[right] > pivot:
            right -= 1
        if left <= right:
            swap(L, left, right)
            left += 1
            right -= 1
    if right >= K:
        quicksort(L, start, right, K)    
    elif left <= K:
        quicksort(L, left, end, K)

quicksort(A, 0, N-1, K)
print(A[K])