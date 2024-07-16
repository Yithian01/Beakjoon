from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n, m, t = map(int, input().split())
# n=인구수, m=키제한, t=망치제한

q = []
for _ in range(n):
    a = int(input())
    heappush(q, (-a))



ans = 0
cnt =0
while t:
    t -= 1
    cnt += 1


    isPass = False
    cn = -heappop(q)
    if cn >= m:
        isPass = True

    if cn > 1:
        cn //= 2
    
    
    if isPass and cn < m:
        ans = max(ans, cnt)
    
    heappush(q, -cn)


cn = -heappop(q)
if cn >= m:
    print('NO')
    print(cn)
else:
    print('YES')
    print(ans)
