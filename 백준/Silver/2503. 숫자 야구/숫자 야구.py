import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input().strip())
Q = [input().split() for _ in range(N)]

A = list(permutations('123456789', 3))
cnt = 0

for i in A:
    status = True
    for q in Q:
        guess = q[0]
        stricks = int(q[1])
        balls = int(q[2])
        
        s = sum(a == b for a, b in zip(i, guess))
        B = sum(a in i for a in guess) - s
        
        if s != stricks or B != balls:
            status = False
            break
    if status:
        cnt += 1

print(cnt)