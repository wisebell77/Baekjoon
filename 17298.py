# 단조 스택

import sys

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
stack = []
result = []

while A:
    if stack:
        if A[-1] < stack[-1]:
            a = A.pop()
            result.append(stack[-1])
            stack.append(a)
        elif A[-1] >= stack[-1]:
            stack.pop()
    else:
        stack.append(A.pop())
        result.append(-1)

result.reverse()
print(*result)