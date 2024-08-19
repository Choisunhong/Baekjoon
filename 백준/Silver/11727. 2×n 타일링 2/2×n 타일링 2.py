import sys
input = sys.stdin.readline
N = int(input().strip()) 

res = [0] * (N+1)
res[1] =1

if N>1:
    res[2]=3

for i in range(3, N + 1):
    res[i] = (res[i-1] + 2*res[i-2]) % 10007
print(res[N])