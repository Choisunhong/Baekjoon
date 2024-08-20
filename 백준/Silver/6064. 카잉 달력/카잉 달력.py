T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    
    found = False
    while x <= M * N:
        if (x - y) % N == 0:
            print(x)
            found = True
            break
        x += M
    
    if not found:
        print(-1)