def count_color(x, y, size):
    global white, blue


    color = paper[x][y]

    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != color:
                small = size // 2
                count_color(x, y, small)
                count_color(x, y + small, small)
                count_color(x + small, y, small)
                count_color(x + small, y + small, small)
                return

    if color == 0:
        white += 1
    else:
        blue += 1

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0
count_color(0, 0, N)

print(white)
print(blue)
