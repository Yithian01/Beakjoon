from collections import deque
import sys
input = sys.stdin.readline
INF = 1e9

#        상      하       좌     우
dir = [(-1, 0),(1, 0),(0, -1), (0, 1)]


m, n = map(int, input().split())
ma = [list(map(int, input().split()))for _ in range(n)]
vi = [[INF] * m for _ in range(n)]

q = deque()
for i in range(n):
    for j in range(m):
        if ma[i][j] == 1:
            q.append((i,j))
            vi[i][j] = 0

        if ma[i][j] == -1:
            vi[i][j] = -1
while q:
    
    cr, cc = q.popleft()
    for dr, dc in dir:
        nr = cr + dr 
        nc = cc + dc 

        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            continue

        if vi[nr][nc] == INF:
            vi[nr][nc] = vi[cr][cc] + 1
            q.append((nr,nc))


ans = -1
for i in range(n):
    for j in range(m):
        if ma[i][j] != -1:
            ans = max(ans, vi[i][j])


if ans == INF:
    print(-1)
else:
    print(ans)