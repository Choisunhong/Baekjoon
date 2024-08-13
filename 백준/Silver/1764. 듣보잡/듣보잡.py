import sys
import math

input =sys.stdin.readline

N,M = map(int,input().strip().split())

A =set(input().strip() for _ in range(N))
B =set(input().strip() for _ in range(M))

C = A & B

res= sorted(C)
print(len(res))
for i in res:
    print(i)
