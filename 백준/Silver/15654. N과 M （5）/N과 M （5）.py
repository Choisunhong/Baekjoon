from itertools import permutations

import sys 
input = sys.stdin.readline
N, M = map(int, input().split())

num = sorted(map(int, input().strip().split()))
comb = permutations(num, M)

for i in comb:
    print(' '.join(map(str, i)))
