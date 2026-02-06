N = input()
A = []
n = len(N)

for i in range(n):
    A.append(int(N[i]))

for i in range(n):
    j = A.index(max(A[i:]), i)
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

print(*A, sep='')