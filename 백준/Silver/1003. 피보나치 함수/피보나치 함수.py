import sys
input = sys.stdin.readline

def fib(n):
    res = [(0, 0)] * (n + 1) 
    res[0] = (1, 0)
    if n > 0:
        res[1] = (0, 1)
    for i in range(2, n + 1):
        res[i] = (res[i - 1][0] + res[i - 2][0], res[i - 1][1] + res[i - 2][1])
    
    return res[n]

N = int(input().strip())
for _ in range(N):
    M = int(input().strip())
    res0, res1 = fib(M) 
    print(res0, res1)
