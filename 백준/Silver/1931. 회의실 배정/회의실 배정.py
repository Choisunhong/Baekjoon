import sys
input = sys.stdin.readline

N = int(input())
rooms = []
for _ in range(N):
    start, end = map(int, input().split())
    rooms.append((start, end))

rooms.sort(key=lambda x: (x[1], x[0]))
count = 0
count_time = 0

for start, end in rooms:
    if start >= count_time:
        count += 1
        count_time = end

print(count)
