import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
visited = [False] * (N)
result = 0

def DFS(start, count):
    global result
    
    if count >= 4:
        result = 1
        return
    
    visited[start] = True
    
    for i in graph[start]:
        if not visited[i]:
            DFS(i, count + 1)
            if result == 1:
                return
            
    visited[start] = False

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N):
    if not visited[i]:
        DFS(i, 0)

print(result)