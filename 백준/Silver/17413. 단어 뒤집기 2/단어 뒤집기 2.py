import sys
input = sys.stdin.readline

S = input().strip()
res = []
word = []
tnf = False

for char in S:
    if char == '<':
        if word:
            res.append(''.join(word)[::-1])
            word = []
        tnf = True
        res.append(char)
    elif char == '>':
        tnf = False
        res.append(char)
    elif tnf:
        res.append(char)
    else:
        if char == ' ':
            res.append(''.join(word)[::-1])
            res.append(char)
            word = []
        else:
            word.append(char)

if word:
    res.append(''.join(word)[::-1])

print(''.join(res))
