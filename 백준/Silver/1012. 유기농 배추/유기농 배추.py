import sys 
sys.setrecursionlimit(10000)
def dfs(x, y, cabbage, check, M, N):

    check[x][y] = True

    if x > 0 and not check[x - 1][y] and cabbage[x - 1][y] == 1:
        dfs(x - 1, y, cabbage, check, M, N)

    if x < M - 1 and not check[x + 1][y] and cabbage[x + 1][y] == 1:
        dfs(x + 1, y, cabbage, check, M, N)

    if y > 0 and not check[x][y - 1] and cabbage[x][y - 1] == 1:
        dfs(x, y - 1, cabbage, check, M, N)

    if y < N - 1 and not check[x][y + 1] and cabbage[x][y + 1] == 1:
        dfs(x, y + 1, cabbage, check, M, N)

T = int(input().strip())

for _ in range(T):
    M, N, K = map(int, input().split())
    cabbage = [[0] * N for _ in range(M)]
    check = [[False] * N for _ in range(M)]
    
    for _ in range(K):
        x, y = map(int, input().split())
        cabbage[x][y] = 1

    count = 0
    
    for i in range(M):
        for j in range(N):
            if cabbage[i][j] == 1 and not check[i][j]:
                dfs(i, j, cabbage, check, M, N)
                count += 1
    
    print(count)