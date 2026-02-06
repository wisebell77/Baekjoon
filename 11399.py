N = int(input())
P = list(map(int, input().split()))
S = [0]*N
Sum = 0

P.sort()
S[0] = P[0]

for i in range(1, N):
    S[i] = S[i-1] + P[i]

for i in S:
    Sum += i

print(Sum)