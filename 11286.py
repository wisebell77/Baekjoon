import sys
from heapq import heappush, heappop

N = int(input())
pos_heap = []
neg_heap = []

for _ in range(N):
    n = int(sys.stdin.readline())
    if n < 0:
        heappush(neg_heap, -n)
    if n > 0:
        heappush(pos_heap, n)
    if n == 0:
        if neg_heap and pos_heap:
            if pos_heap[0] < neg_heap[0]:
                print(heappop(pos_heap))
            elif neg_heap[0] < pos_heap[0]:
                print(-heappop(neg_heap))
            elif neg_heap[0] == pos_heap[0]:
                print(-heappop(neg_heap))
        elif neg_heap:
            print(-heappop(neg_heap))
        elif pos_heap:
            print(heappop(pos_heap))
        else:
            print(0)