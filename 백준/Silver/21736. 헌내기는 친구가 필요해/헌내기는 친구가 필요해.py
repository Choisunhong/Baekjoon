from collections import deque

N, M = map(int, input().split())
campus = []
for _ in range(N):
    campus.append(list(input().strip()))
# 도연위치
x = y = 0
for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            x, y = i, j
            break

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y):
    queue = deque([(x, y)])
    visited = set()
    visited.add((x, y))
    count = 0

    while queue:
        current_x, current_y = queue.popleft()

        for dx, dy in directions:
            nx, ny = current_x + dx, current_y + dy
            if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited:
                if campus[nx][ny] != 'X':  # 벽이 아니라면
                    visited.add((nx, ny))
                    queue.append((nx, ny))
                    if campus[nx][ny] == 'P':  # 사람이라면
                        count += 1
    
    return count

result = bfs(x, y)

if result == 0:
    print("TT")
else:
    print(result)