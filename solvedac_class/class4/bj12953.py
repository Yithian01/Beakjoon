from collections import deque
import sys
input = sys.stdin.readline
INF = 2e9
q = deque()


st, m = map(int, input().split())
q.append((1, st))
ans = INF



cnt = 0 
while q:
    cw, cn = q.popleft()

    an = cn * 2
    bn = str(cn) + '1'
    bn = int(bn)

    
    if an == m:
        ans = min(ans, cw + 1)
        break
    if bn == m :
        ans = min(ans, cw + 1)
        break



    if an < m:
        q.append((cw + 1, an))
    if bn < m:
        q.append((cw + 1, bn))
      


if ans == INF:
    print(-1)
else:
    print(ans)