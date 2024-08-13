import sys
input =sys.stdin.readline
N = int(input().strip())

lst = list(map(int, input().strip().split()))
lst.sort()
res=0
time= 0
for i in lst:
    time +=i
    res += time
print(res)

