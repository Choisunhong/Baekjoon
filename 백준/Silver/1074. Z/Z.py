import sys
input = sys.stdin.readline

def zigzag(n, r, c):
    if n == 0:
        return 0
    
    half = 2 ** (n - 1)
    if r < half and c < half: 
        return zigzag(n - 1, r, c)
    elif r < half and c >= half: 
        return half * half + zigzag(n - 1, r, c - half)
    elif r >= half and c < half: 
        return 2 * half * half + zigzag(n - 1, r - half, c)
    else:  #
        return 3 * half * half + zigzag(n - 1, r - half, c - half)

n, r, c = map(int, input().split())

print(zigzag(n, r, c))
