from collections import deque
import sys
input = sys.stdin.readline

def bfs(n, m, Map):
    # 거리 저장 리스트 초기화
    distance = [[-1] * m for _ in range(n)]
    

    start_x, start_y = -1, -1
    for i in range(n):
        for j in range(m):
            #2를 만날때
            if Map[i][j] == 2:
                start_x, start_y = i, j
                break
        if start_x != -1:
            break

    queue = deque([(start_x, start_y)])
    distance[start_x][start_y] = 0
    
    while queue:
        x, y = queue.popleft()
        #상
        if x - 1 >= 0 and Map[x - 1][y] == 1 and distance[x - 1][y] == -1:  
            distance[x - 1][y] = distance[x][y] + 1
            queue.append((x - 1, y))
        #하
        if x + 1 < n and Map[x + 1][y] == 1 and distance[x + 1][y] == -1: 
            distance[x + 1][y] = distance[x][y] + 1
            queue.append((x + 1, y))
        #좌
        if y - 1 >= 0 and Map[x][y - 1] == 1 and distance[x][y - 1] == -1:  
            distance[x][y - 1] = distance[x][y] + 1
            queue.append((x, y - 1))
        #우
        if y + 1 < m and Map[x][y + 1] == 1 and distance[x][y + 1] == -1:  
            distance[x][y + 1] = distance[x][y] + 1
            queue.append((x, y + 1))
    
    for i in range(n):
        for j in range(m):
            if Map[i][j] == 0:  # 0을 만난순간
                print(0, end=" ")
            else:
                print(distance[i][j], end=" ")
        print()

n, m = map(int, input().split())
Map = []
for _ in range(n):
    Map.append(list(map(int, input().split())))

# BFS 실행 및 결과 출력
bfs(n, m, Map)
