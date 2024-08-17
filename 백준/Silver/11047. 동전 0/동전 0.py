import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))

count = 0

coins.sort(reverse=True)

for coin in coins:
    if K == 0:
        break
    count += K // coin 
    K %= coin 
print(count)
