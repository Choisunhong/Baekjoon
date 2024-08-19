import sys 
input = sys.stdin.readline

lst = input().strip()

min = lst.split('-')

res = sum(map(int,min[0].split('+'))) - sum(sum(map(int,plus.split('+')))for plus in min[1:])

print(res)