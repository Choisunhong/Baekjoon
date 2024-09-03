import sys
input = sys.stdin.readline

N = int(input().strip())
board = [list(input().strip()) for _ in range(N)]

def check(board):
    len = 1
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if board[i][j] == board[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
            len = max(len, cnt)
    for j in range(N):
        cnt = 1
        for i in range(1, N):
            if board[i][j] == board[i - 1][j]:
                cnt += 1
            else:
                cnt = 1
            len = max(len, cnt)
    return len

res = 1

for i in range(N):
    for j in range(N):
        if j + 1 < N:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            res = max(res, check(board))
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
        if i + 1 < N:
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            res = max(res, check(board))
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

print(res)
