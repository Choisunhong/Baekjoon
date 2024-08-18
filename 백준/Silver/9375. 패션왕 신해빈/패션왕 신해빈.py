import sys

input = sys.stdin.readline

# 테스트 케이스의 수
N = int(input())

for _ in range(N):
    n = int(input())
    
    if n == 0:
        print(0)
        continue
    clothes = {}

    for _ in range(n):
        name, type = input().split()
        if type in clothes:
            clothes[type] += 1
        else:
            clothes[type] = 1
    result = 1
    for count in clothes.values():
        # 해당 종류의 옷을 입지 않는 경우를 포함
        result *= (count + 1)  
    #맨몸일때 케이스 하나 빼주기
    print(result-1)
