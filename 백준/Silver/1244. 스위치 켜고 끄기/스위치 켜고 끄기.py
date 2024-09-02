import sys 
input = sys.stdin.readline

N = int(input())
switch = list(map(int,input().split()))
student_num= int(input())

for _ in range(student_num):
    gender,number=map(int,input().split()) 

    if gender == 1: 
        for i in range(number - 1, N, number):
            switch[i] = 1 - switch[i]
    
    elif gender == 2: 
        left = right = number - 1
        while left >= 0 and right < N and switch[left] == switch[right]:
            left -= 1
            right += 1
        left += 1
        right -= 1
        for i in range(left, right + 1):
            switch[i] = 1 - switch[i]
for i in range(0, N, 20):
    print(" ".join(map(str, switch[i:i+20])))