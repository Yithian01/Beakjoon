# n이 작아서 조합을 

# 시간복잡도 계산: Mc1 + Mc2 . . . McM => 2^n
from itertools import combinations
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
q = []
for _ in range(m):
    a = list(map(int,input().split()))
    tmp = 0
    for i in a[1:]:
        tmp |= 1 << (i-1)
    
    q.append(tmp)


ans = -1
res = (1 << n) -1
isGo = False

for i in range(1, m):
    for com in combinations([ _ for _ in range(m)], i):
        tmp = 0
        for j in com:
            tmp |= q[j]

        if tmp == res:
            ans = i
            isGo = True
            break
    
    if isGo:
        break

print(ans)