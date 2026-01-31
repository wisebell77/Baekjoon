from __future__ import annotations
from collections import deque
import sys

N, L = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
A: deque = deque()
B: deque = deque()
D = []

for i in range(N):
    A.append([i+1, a[i]])

B.append(A.popleft())
D.append(B[0][1])

def compare(b: list):
    if b[0] - B[0][0] >= L:
        B.popleft()
    while B:
        if B[-1][1] > b[1]:
            B.pop()
        else:
            break
    B.append(b)
    D.append(B[0][1])

while A:
    b = A.popleft()
    compare(b)

print(*D)


# 답지 풀이
# from collections import deque
# N, L = map(int, input().split())
# mydeque = deque()
# now = list(map(int, input().split()))

# for i in range(N):
#     while mydeque and mydeque[-1][0] > now[i]:
#         mydeque.pop()
#     mydeque.append((now[i], i))
#     if mydeque[0][1] <= i - L:
#         mydeque.popleft()
#     print(mydeque[0][0], end=' ')