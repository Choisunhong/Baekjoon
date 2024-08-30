import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
index = 2


A = []
for i in range(N):
    A.append([int(x) for x in data[index:index+N]])
    index += N

S = [[0] * (N + 1) for _ in range(N + 1)]


for i in range(1, N+1):
    for j in range(1, N+1):
        S[i][j] = A[i-1][j-1] + S[i-1][j] + S[i][j-1] - S[i-1][j-1]


for _ in range(M):
    x1 = int(data[index])
    y1 = int(data[index+1])
    x2 = int(data[index+2])
    y2 = int(data[index+3])
    index += 4
    
    result = S[x2][y2] - S[x1-1][y2] - S[x2][y1-1] + S[x1-1][y1-1]
    print(result)
