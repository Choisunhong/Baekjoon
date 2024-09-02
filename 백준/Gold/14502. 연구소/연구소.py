from itertools import combinations
from collections import deque
import copy
import sys 
input = sys.stdin.readline

N,M = map(int,input().split())

lab = []
for _ in range(N):
    lab.append(list(map(int, input().split())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

empty = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 0]
virus = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 2]

res = 0

for walls in combinations(empty, 3):

    temp_lab = [row[:] for row in lab]
    
    for wall in walls:
        temp_lab[wall[0]][wall[1]] = 1
    

    queue = deque(virus)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and temp_lab[nx][ny] == 0:
                temp_lab[nx][ny] = 2
                queue.append((nx, ny))

    num = 0
    for i in range(N):
        for j in range(M):
            if temp_lab[i][j] == 0:
                num += 1

    if num > res:
        res = num

print(res)