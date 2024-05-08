# 이렇게 쉬울 리가 없는데...
from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
num = [0] + list(map(int, input().split()))
ma = [[] for _ in range(n+1)]

for _ in range(r):
    s, e, t = map(int, input().split())
    ma[s].append((t,e))
    ma[e].append((t,s))

ans = 0
for i in range(1, n+1):
    vi = [False] * (n+1)
    q = deque()
    q.append((0, i))
    res = 0

    while q:
        we, cn = q.popleft()
        
        vi[cn] = True
        for gwe, nn in ma[cn]:
            tmp = we + gwe
            if tmp <= m:
                q.append((tmp , nn))


    for j in range(1, n+1):
        if vi[j]:
            res += num[j]
    ans = max(ans, res)
print(ans)