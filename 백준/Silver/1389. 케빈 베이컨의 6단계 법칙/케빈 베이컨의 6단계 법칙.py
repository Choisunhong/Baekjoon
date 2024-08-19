from collections import deque
import sys

input = sys.stdin.readline


N, M = map(int, input().split())


graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

def bfs(start):
    # 각 노드의 거리를 저장
    num = [-1] * (N + 1)  
    queue = deque([start])
    num[start] = 0  # 시작점의 거리는 0

    while queue:
        current = queue.popleft()

        for neighbor in graph[current]:
            if num[neighbor] == -1:  # 아직 방문하지 않은 노드
                num[neighbor] = num[current] + 1
                queue.append(neighbor)

    return sum(res for res in num if res != -1)

bacon = sys.maxsize
person = 0

for i in range(1, N + 1):
    bacon_sum = bfs(i)
    if bacon_sum < bacon:
        bacon = bacon_sum
        person = i

print(person)
