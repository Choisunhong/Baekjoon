import sys 
input = sys.stdin.readline
A, B, C = map(int, input().split())

result = 1
base = A % C

while B > 0:
    if B % 2 == 1:  
        result = (result * base) % C
    base = (base * base) % C
    B //= 2

print(result)
