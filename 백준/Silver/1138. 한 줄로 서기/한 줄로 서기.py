import sys 
input = sys.stdin.readline
N = int(input())
height = list(map(int, input().split()))

res = [-1] * N

for i in range(N):
    count = height[i]
    for j in range(N):
        if res[j] == -1: 
            if count == 0:
                res[j] = i + 1  
                break
            count -= 1

print(' '.join(map(str, res)))
