num = []

for _ in range(9):
    n = int(input())
    num.append(n)

m = max(num)
print(m)
print(num.index(m) + 1)