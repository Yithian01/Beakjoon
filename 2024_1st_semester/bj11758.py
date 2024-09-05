# 외적을 통해 A, B 에 대해 C가 시계, 반시계, 일직선상에 있는지 알 수 있다.

import sys
input = sys.stdin.readline

a = list(map(int, input().split()) ) 
b = list(map(int, input().split()) ) 
c = list(map(int, input().split()) ) 


ans = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

if ans > 0:
    print(1)
elif ans == 0:
    print(0)
else:
    print(-1)

