import sys
input =sys.stdin.readline

tri = [0]*101

tri [1] =1
tri [2] =1
tri [3] =1
tri [4] =2
tri [5] =2

for i in range(6,101):
    tri[i] = tri[i-1] + tri[i-5] 
T = int(input())
for _ in range(T):
    N = int(input())
    print(tri[N])