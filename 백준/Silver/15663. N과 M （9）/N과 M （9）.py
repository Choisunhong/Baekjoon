import sys 
input = sys.stdin.readline
from itertools import permutations

N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))

nandm = sorted(set(permutations(num, M)))

for i in nandm:
    print(" ".join(map(str, i)))
