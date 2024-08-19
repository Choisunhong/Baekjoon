import sys 
input = sys.stdin.readline
def dfs(x, y):

    if x < 0 or x >= N or y < 0 or y >= N:
        return 0
  
    if house[x][y] == 1:
        house[x][y] = 0  
        count = 1  
 
        count += dfs(x - 1, y)  
        count += dfs(x + 1, y)  
        count += dfs(x, y - 1)  
        count += dfs(x, y + 1)  
        
        return count
    return 0

N = int(input())
house = [list(map(int, input().strip())) for _ in range(N)]

house_count = []

for i in range(N):
    for j in range(N):
        size = dfs(i, j)
        if size > 0:
            house_count.append(size)

house_count.sort()
print(len(house_count))
for size in house_count:
    print(size)
