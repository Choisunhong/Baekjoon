import sys
input = sys.stdin.readline
s = input().strip()

stack = []
result = 0
temp = 1

for i in range(len(s)):
    if s[i] == '(':
        stack.append('(')
        temp *= 2
    elif s[i] == '[':
        stack.append('[')
        temp *= 3
    elif s[i] == ')':
        if not stack or stack[-1] != '(':
            print(0)
            exit()
        if s[i-1] == '(':
            result += temp
        stack.pop()
        temp //= 2
    elif s[i] == ']':
        if not stack or stack[-1] != '[':
            print(0)
            exit()
        if s[i-1] == '[':
            result += temp
        stack.pop()
        temp //= 3

if stack:
    print(0)
else:
    print(result)
