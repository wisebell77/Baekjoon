n, m = map(int, input().split())
friend = {}
for i in range(1, n + 1):
    friend[i] = 0
for i in range(m):
    a, b = map(int, input().split())
    friend[a] += 1
    friend[b] += 1
for i in friend:
    print(friend[i])