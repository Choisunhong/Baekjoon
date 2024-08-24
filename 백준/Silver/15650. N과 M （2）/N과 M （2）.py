from itertools import combinations
import sys 
input = sys.stdin.readline

N, M = map(int, input().split())

comb = combinations(range(1, N + 1), M)

for i in comb:
    print(' '.join(map(str, i)))