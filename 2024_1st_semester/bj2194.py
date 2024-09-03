from collections import deque
import sys
input = sys.stdin.readline
dir = [(-1, 0),(1, 0),(0, -1),(0, 1)]
INF= 1e9


n, m, a, b, k = map(int, input().split())
ma = [[0] * (m + 1) for _ in range(n+1)]
vi = [[INF] * (m + 1) for _ in range(n+1)]

q = deque()
for _ in range(k):
    r, c = map(int, input().split())
    ma[r][c] = -1

sr, sc = map(int, input().split())
q.append((sr,sc))
vi[sr][sc] = 0

er, ec = map(int, input().split())


while q:
    
    cr, cc= q.popleft()

   
    for dr, dc in dir:
        nr = cr + dr 
        nc = cc + dc

        isPass = False

        if nr <= 0 or nr > n or nc <= 0 or nc > m:
            continue
        
        for i in range(nr, nr + a):
            for j in range(nc, nc + b):

                if i <= 0 or i > n or j <= 0 or j > m:
                    isPass = True
                    break
                
                if ma[i][j] == -1:
                    isPass = True
                    break
            
            if isPass:
                break

        if isPass:
            continue

        if vi[nr][nc] > vi[cr][cc] + 1:
            vi[nr][nc] = vi[cr][cc] + 1
            q.append((nr,nc))


if vi[er][ec] != INF:
    print(vi[er][ec])
else:
    print(-1)