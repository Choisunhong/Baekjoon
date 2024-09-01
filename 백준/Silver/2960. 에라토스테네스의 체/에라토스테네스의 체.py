import sys
input = sys.stdin.readline

N, K = map(int, input().split())

num = [True] * (N + 1)  
count = 0

for i in range(2, N + 1):
    if num[i]:
        for j in range(i, N + 1, i):
            if num[j]:
                num[j] = False  
                count += 1
                if count == K:
                    print(j)
                    exit()
