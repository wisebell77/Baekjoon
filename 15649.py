N, M = map(int, input().split())
visited = [False] * N
series = []
result = []

def backtracker(num):
    global series
    
    visited[num] = True
    series.append(num)

    if len(series) == M:
        result.append([x+1 for x in series])
        visited[num] = False
        series.pop()
        return
    
    for i in range(N):
        if not visited[i]:
            backtracker(i)

    visited[num] = False
    series.pop()

for i in range(N):
    backtracker(i)

for i in result:
    print(*i)