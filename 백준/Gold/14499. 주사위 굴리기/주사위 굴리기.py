import sys
input = sys.stdin.readline
N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))


dice = [0] * 6  

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def roll_dice(direction):
    if direction == 1: 
        dice[0], dice[2], dice[5], dice[3] = dice[3], dice[0], dice[2], dice[5]
    elif direction == 2: 
        dice[0], dice[3], dice[5], dice[2] = dice[2], dice[0], dice[3], dice[5]
    elif direction == 3:  
        dice[0], dice[1], dice[5], dice[4] = dice[4], dice[0], dice[1], dice[5]
    elif direction == 4:  
        dice[0], dice[4], dice[5], dice[1] = dice[1], dice[0], dice[4], dice[5]

for command in commands:
    nx = x + dx[command - 1]
    ny = y + dy[command - 1]
    
    if not (0 <= nx < N and 0 <= ny < M):
        continue
   
    x, y = nx, ny

    roll_dice(command)

    if board[x][y] == 0:
        board[x][y] = dice[5]
    else:
        dice[5] = board[x][y]
        board[x][y] = 0

    print(dice[0])
