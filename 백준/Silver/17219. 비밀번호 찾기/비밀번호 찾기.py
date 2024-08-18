import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dic = {}

for _ in range(N):
    site,pw = input().split()
    dic[site] = pw

for _ in range(K):
    site = input().strip()
    print(dic[site])
