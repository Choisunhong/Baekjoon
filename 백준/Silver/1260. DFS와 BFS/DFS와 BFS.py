from collections import deque
import sys
input = sys.stdin.readline
def dfs(graph,start,visit):
    visit[start] =True
    print(start, end=' ')
    for next in sorted(graph[start]):
        if not visit[next]:
            dfs(graph,next,visit)

def bfs(graph,start):
    visit =[False]*(len(graph)+1)
    queue = deque([start])
    visit[start] = True
    while queue:
        res = queue.popleft()
        print(res, end=' ')
        for next in sorted(graph[res]):
            if not visit[next]:
                queue.append(next)
                visit[next] = True
N,M,V = map(int,input().strip().split())

graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    u, v = map(int, input().strip().split())
    graph[u].append(v)
    graph[v].append(u)

visit = [False] * (N + 1)
dfs(graph, V, visit)
print()

bfs(graph, V)