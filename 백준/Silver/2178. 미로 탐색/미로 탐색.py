from collections import deque

def bfs(maze, n, m):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(0, 0)])
    maze[0][0] = 1  
    
    while queue:
        x, y = queue.popleft()
        if x == n - 1 and y == m - 1:
            return maze[x][y]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            #1인 값 발견하면 append
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

N,M= map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]

print(bfs(maze, N, M))