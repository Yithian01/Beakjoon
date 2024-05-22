from collections import deque
import sys
input = sys.stdin.readline
dir = [(-1, 0),(1, 0),(0, -1),(0, 1)]


n ,m  = map(int, input().split())
ma = [list(map(int, input().split()))for _ in range(n)]
t = int(input())

ans = 0
vi = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(0, m * 3, 3):
        avg = sum(ma[i][j:j+3]) // 3
        if avg >= t:
            if j == 0 :
                vi[i][j] = 1
            else:
                vi[i][j // 3] = 1

dp = [[False] * m for _ in range(n)]
def bfs(r, c):
    q = deque()
    q.append((r,c))
    
    while q:
        cr, cc = q.popleft()
        for dr, dc in dir:
            nr = cr + dr 
            nc = cc + dc 

            if nr < 0 or nr >= n or nc < 0 or nc >= m :
                continue
            
            if vi[nr][nc] == 1 and not dp[nr][nc]:
                dp[nr][nc] = True
                q.append((nr,nc))

    return 




for i in range(n):
    for j in range(m):
        if vi[i][j] == 1 and not dp[i][j]:
            ans += 1
            bfs(i,j) 


print(ans)