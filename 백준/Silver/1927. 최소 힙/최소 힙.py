import heapq
import sys
#제일 윗단 트리에 최솟값 넣어두기
input = sys.stdin.readline

heap = []
N = int(input().strip())

for _ in range(N):
    x = int(input().strip())
    
    if x > 0:
        heapq.heappush(heap, x)
    elif x == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
