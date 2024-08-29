from collections import deque
import sys 
input = sys.stdin.readline
N = int(input())

tree = [[] for _ in range(N + 1)]
parent = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


def bfs(M):
    queue = deque([M])
    parent[M] = -1  
    while queue:
        node = queue.popleft()
        for neighbor in tree[node]:
            if parent[neighbor] == 0:  
                parent[neighbor] = node  
                queue.append(neighbor)

bfs(1)


for i in range(2, N + 1):
    print(parent[i])
