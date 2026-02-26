import sys

input = sys.stdin.readline

N = int(input())
num = [0] * (10001)

for _ in range(N):
    i = int(input())
    num[i] += 1

for i in range(10001):
    while num[i] != 0:
        print(i)
        num[i] -= 1