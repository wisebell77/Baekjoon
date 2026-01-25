n = int(input())
num = []
for _ in range(n):
    a = int(input())
    num.append(a)
for _ in range(n):
    t = min(num)
    print(t)
    num.remove(t)