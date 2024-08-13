import sys 

N = int(sys.stdin.readline())
A=set(map(int,sys.stdin.readline().strip().split()))

M = int(sys.stdin.readline())
B=list(map(int,sys.stdin.readline().strip().split()))
for h in B:
    print(1) if h in A else print(0)