import sys 
input = sys.stdin.readline
from collections import Counter

hansoo = input().strip()
cnt = Counter(hansoo)
alpa = ''
change = ''

for name, num in sorted(cnt.items()):
    if num % 2 != 0:
        if alpa:
            print("I'm Sorry Hansoo")
            exit()
        alpa = name
    change += name * (num // 2)

res = change + alpa + change[::-1]
print(res)
