import sys
input = sys.stdin.readline

res = [0] * 12  
res[1] = 1
res[2] = 2
res[3] = 4

for i in range(4, 12):
    res[i] = res[i-1] + res[i-2] + res[i-3]

N = int(input().strip()) 
for _ in range(N):
    n = int(input())
    print(res[n])
