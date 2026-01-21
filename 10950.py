t = int(input())
cal = list()
for i in range(1, t + 1):
    a, b = map(int, input().split())
    cal.append(a + b)
for i in cal:
    print(i)