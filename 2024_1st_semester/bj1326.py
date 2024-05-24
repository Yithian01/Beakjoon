from collections import deque
import sys
input = sys.stdin.readline
INF = 2e9

n = int(input())
ma =[0] + list(map(int, input().split()))
st, ed = map(int, input().split())


dq = deque()
dq.append((0, st))
vi = [INF] * (n+1)
vi[st] = 0

ans = -1
while dq:
    cw , cn = dq.popleft()
    if cn == ed:
        ans = cw
        break

    for i in range(1, n):
        dn = cn - (ma[cn] * i)
        un = cn + (ma[cn] * i)


        if 0 < dn  :
            dq.append((cw + 1, dn))
        
        if un <= n :
            dq.append((cw + 1, un))



print(ans)