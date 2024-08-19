from collections import deque ,Counter
import sys
input = sys.stdin.readline

N = int(input())

fruits = list(map(int, input().split())) 
max_length = 0
left = 0

fruit_count = Counter()
#{1:1개 , 2: 3개} 이런식으로 저장됨

for right in range(N):
    #Right를 하나씩 증가시키며 과일 숫자 세기
    fruit_count[fruits[right]] += 1

    while len(fruit_count) > 2:
        #첫번쨰 날리기
        fruit_count[fruits[left]] -= 1
        if fruit_count[fruits[left]] == 0:
            del fruit_count[fruits[left]]
        left += 1

    max_length = max(max_length, right - left + 1)

            
print(max_length)
