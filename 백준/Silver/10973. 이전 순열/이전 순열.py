N = int(input())
perm = list(map(int, input().split()))

i = N - 2
while i >= 0 and perm[i] <= perm[i + 1]:
    i -= 1

if i == -1:
    print(-1)
else:
    j = N - 1
    while perm[i] <= perm[j]:
        j -= 1
    
    perm[i], perm[j] = perm[j], perm[i]
    
    perm = perm[:i+1] + sorted(perm[i+1:], reverse=True)
    
    print(' '.join(map(str, perm)))
