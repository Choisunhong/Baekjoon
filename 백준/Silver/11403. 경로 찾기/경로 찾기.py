import sys
input = sys.stdin.readline

N = int(input().strip())
graph = [list(map(int, input().split())) for _ in range(N)]

#3중 포문으로 경로 찾기(플로이드-워셜)
# 그래프의 값이1이 되는 경우는 
# 직접연결 or 중간다리 있는거
for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1

for row in graph:
    print(" ".join(map(str, row)))