#1) 조합 구하기 -> 대피소 위치
#2) 각 집에서 가장 가까운 대피소 구하기
#3) (2)에서 구한 것들중 최고값이 ans 
 
# 시간 복잡도 계산: 50C3 * 50 * 3 => 19800 * 150 = > 19 * 10^3 * 10^2 => 1 * 10^6 정도
from itertools import combinations
import sys
input = sys.stdin.readline
INF = 1e9

n, k = map(int, input().split())
ma = []
for _ in range(n):
    c, r = map(int, input().split())
    ma.append((c,r))    

ma.sort()
ans =  INF
for com in combinations( range(n) , k): # 대피소 가능 
    a = [ i for i in range(n) if i not in com ] # 다른 집들 
    
    cnt = 0
    for i in a:
        tmp = INF
        for j in com:
            tmp = min(tmp, abs(ma[i][0] - ma[j][0]) + abs(ma[i][1] - ma[j][1]) )

        cnt = max(cnt, tmp)

    ans = min(ans, cnt)

print(ans)