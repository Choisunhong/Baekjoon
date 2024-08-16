import sys
input = sys.stdin.readline
N,M = map(int,input().strip().split())

poke = {}

for i in range(1, N + 1):
    name = input().strip()
    #숫자를 키로 사용
    poke[str(i)] = name  
    #이름을 키로 사용
    poke[name] = i        

for _ in range(M):
    query = input().strip()
    print(poke[query])