from collections import deque
import sys
input = sys.stdin.readline

T = int(input().strip())  

for _ in range(T):
    p = input().strip()  
    n = int(input().strip())  
    lst = input().strip()[1:-1]  
    #빈베열 췌크
    if lst:  
        arr = deque(map(int, lst.split(',')))
    else:  
        arr = deque()
    
    reverse = False  
    error_flag = False  
    
    for cmd in p:
        if cmd == 'R':  
            reverse = not reverse
        elif cmd == 'D':  
            if not arr:  
                error_flag = True
                break
            if reverse:
                arr.pop()  
            else:
                arr.popleft() 
    
    if error_flag:
        print("error")
    else:
        if reverse:
            arr.reverse()
        print("[" + ",".join(map(str, arr)) + "]")
