import sys
input = sys.stdin.readline
N, W, L = map(int, input().split())
trucks = list(map(int, input().split()))

time = 0
bridge = [0] * W
num = 0

for truck in trucks:
    while True:
        time += 1
        num -= bridge.pop(0)
        if num + truck <= L:
            bridge.append(truck)
            num += truck
            break
        else:
            bridge.append(0)

time += W
print(time)
