import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append((nx, ny))

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i, j))
bfs()
day=0
yes=True

for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            yes = False
        day = max(day, box[i][j])
if not yes:
    print(-1)
elif day == 1:
    print(0)
else:
    print(day - 1)