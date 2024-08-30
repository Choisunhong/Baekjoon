import sys 
input = sys.stdin.readline

N, K = map(int, input().split())
items = []
for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V))

dp = [0] * (K + 1)

for W, V in items:
    for w in range(K, W - 1, -1):
        dp[w] = max(dp[w], dp[w - W] + V)

print(dp[K])
