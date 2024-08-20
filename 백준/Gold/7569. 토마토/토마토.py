from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
tomato = []
for _ in range(H):
    box = [list(map(int, input().split())) for _ in range(N)]
    tomato.append(box)

queue = deque()
directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
days = 0

for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomato[h][n][m] == 1:
                queue.append((h, n, m))


while queue:
    h, n, m = queue.popleft()
    for dh, dn, dm in directions:
        nh, nn, nm = h + dh, n + dn, m + dm
        if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M:
            if tomato[nh][nn][nm] == 0:
                tomato[nh][nn][nm] = tomato[h][n][m] + 1
                queue.append((nh, nn, nm))

for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomato[h][n][m] == 0:
                print(-1)
                exit(0)
            days = max(days, tomato[h][n][m])

print(days-1)
