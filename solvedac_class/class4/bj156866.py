from collections import deque
import itertools
import sys
input = sys.stdin.readline
dir = [(-1, 0),(1, 0),(0, -1),(0, 1)]
INF = 1e9

def bfs(pq):
    vi = [[INF] * n for _ in range(n)]
    dq = deque()
    for i in pq:
        r, c = s[i]
        vi[r][c] = 0
        dq.append((r,c))
        
    while dq:
        cr, cc = dq.popleft()
        for dr, dc in dir:
            nr = cr + dr
            nc = cc + dc 

            if nr < 0 or nr >= n or nc < 0 or nc >= n: continue
            
            if vi[nr][nc] > vi[cr][cc] + 1:
                vi[nr][nc] = vi[cr][cc] + 1
                dq.append((nr,nc))

    tmp = 0
    for i in range(n):
        for j in range(n):
            if ma[i][j] ==1:
                tmp += vi[i][j]

    return tmp
            
    

n, m = map(int, input().split())
ma = [list(map(int, input().split()))for _ in range(n)]
h = []
s = []

for i in range(n):
    for j in range(n):
        if ma[i][j] == 1:
            h.append([i,j])
        
        if ma[i][j] == 2:
            s.append([i,j])

q = list(itertools.combinations(range(len(s)), m))

ans = INF
for i in range(len(q)):
    ans = min(ans, bfs(q[i]))

print(ans)