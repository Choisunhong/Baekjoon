import sys
input =sys.stdin.readline
def find_max_height(trees, M):
    start, end = 0, max(trees)
    result = 0

    while start <= end:
        mid = (start + end) // 2
        total = sum(tree - mid if tree > mid else 0 for tree in trees)

        if total >= M:
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    return result


N, M = map(int, input().split())
trees = list(map(int, input().split()))

print(find_max_height(trees, M))
