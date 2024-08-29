import sys 
input = sys.stdin.readline
N = int(input())  
price = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N)]

dp[0][0] = price[0][0]
dp[0][1] = price[0][1]
dp[0][2] = price[0][2]

for i in range(1, N):
    #R
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + price[i][0]  
    #G
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + price[i][1]  
    #B
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + price[i][2]  

print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))
