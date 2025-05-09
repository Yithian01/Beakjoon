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

    
    투 포인터: outer, inner를 잡는다. 
        outer = [0, 3]
        inner = [1, 2]

        outer의 차이는 3차이가 난다.
        i = 0 ~ n-3   시작
        j = i+3 ~ n   끝 

        inner는 outer의 내부를 투포인터로 탐색 
        le = i+1
        ri = j-1
        
        눈사람A = i+j    ( out )
        눈사람B = le+ri  ( in)
        
        정렬했을 경우 오른쪽으로 갈수록 크기가 커진다.
        if out > in 이라면 in을 키워야 하므로 le += 1
        if out < in 이라면 in을 작게해야 하므로 ri -= 1

    
    시간복잡도 계산: O(N LogN) 정도


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
