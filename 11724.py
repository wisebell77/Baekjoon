import sys

input = sys.stdin.readline

def DFS(start):
    stack.append(start)
    while stack:
        temp = stack.pop()
        if visited[temp] == 0:
            visited[temp] = 1
            for i in graph[temp]:
                stack.append(i)

N, M = map(int, input().split())

stack = []
graph = [[] for _ in range(N+1)]
visited = {}
cc = 0

for i in range(1, N+1):
    visited[i] = 0

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    if visited[i] == 0:
        DFS(i)
        cc += 1

print(cc)