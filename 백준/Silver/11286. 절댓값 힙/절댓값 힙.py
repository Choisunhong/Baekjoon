import heapq
import sys

input = sys.stdin.read
data = input().split()
N = int(data[0])

heap = []
index = 1

for _ in range(N):
    x = int(data[index])
    index += 1
    
    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)