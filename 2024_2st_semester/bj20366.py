import sys
from itertools import combinations
input = sys.stdin.readline
INF = sys.maxsize
'''
    눈사람 2개 만들기 a, b
    | a - b | 가 작을수록 좋다.

    숫자쌍을 두개 만들고 그 차이가 적게 만들어라 
    조합? -> 시간초과 
    브루트포스 -> 시간 초과 4중 for문으로 하면 터짐

    절반을 나누고 그 절반끼리 매칭

'''
n = int(input())
ma = list(map(int, input().split()))
ma.sort()

ans = abs( (ma[0] + ma[3]) - (ma[1] + ma[2]))
for i in range(n-3): # 바깥쪽 st 의 최대 이동 거리 
    for j in range(i + 3, n): # 바깥쪽 ed 의 최대 이동 거리
        outer = ma[i] + ma[j] # <--- 바깥쪽 합 

        le = i + 1 # 내부 st
        ri = j - 1 # 내부 ed 

        while le < ri:
            inner = ma[le] + ma[ri]
            diff = abs(outer - inner)
            ans = min(ans, diff)
            if ans == 0:
                print(0)
                exit(0)
            
            if inner > outer:
                ri -= 1
            else:
                le += 1
                
            
print(ans)
