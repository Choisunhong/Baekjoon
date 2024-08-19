import sys 
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().strip()
res = 0 
i = 0
while i < (M - 1):

    if S[i:i+3] == "IOI":
        count = 0
        while i + 2 < M and S[i+1:i+3] == "OI": 
            count += 1
            i += 2
        if count >= N:  
            res += (count - N + 1)
        i += 1  
    else:
        i += 1

print(res)