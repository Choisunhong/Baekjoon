import sys 
input = sys.stdin.readline

N = int(input())
students = {}
grid = [[0] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N * N):
    data = list(map(int, input().split()))
    students[data[0]] = data[1:]

for student in students:
    preferences = students[student]
    best_pos = (-1, -1)
    max_like = -1
    max_empty = -1

    for r in range(N):
        for c in range(N):
            if grid[r][c] == 0: 
                like_count = 0
                empty_count = 0

                for i in range(4):
                    nx = r + dx[i]
                    ny = c + dy[i]
                    if 0 <= nx < N and 0 <= ny < N:
                        if grid[nx][ny] in preferences:
                            like_count += 1
                        if grid[nx][ny] == 0:
                            empty_count += 1
                
                if (like_count > max_like or 
                    (like_count == max_like and empty_count > max_empty) or
                    (like_count == max_like and empty_count == max_empty and best_pos == (-1, -1))):
                    best_pos = (r, c)
                    max_like = like_count
                    max_empty = empty_count

    grid[best_pos[0]][best_pos[1]] = student

res = 0
for r in range(N):
    for c in range(N):
        student = grid[r][c]
        preferences = students[student]
        like_count = 0

        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if grid[nx][ny] in preferences:
                    like_count += 1
        if like_count > 0:
            res += 10 ** (like_count - 1)

print(res)
