from collections import deque
import sys
input = sys.stdin.readline
dir = {'U':(-1, 0), 'D':(1, 0), 'L':(0, -1), 'R':(0,1)}




def BFS(r, c, t):
    global ans
    q = deque()
    q.append((r,c))
    
    while q:
        cr, cc = q.popleft()
        dr, dc = dir[ma[cr][cc]]
        
        nr = cr + dr 
        nc = cc + dc 

        if vi[nr][nc] == t:
            ans +=1
            return
        

        if vi[nr][nc] == 0:
            vi[nr][nc] = t
            
            q.append((nr,nc))

        else:
            return 

n, m = map(int, input().split())
ma = [list(input().rstrip()) for _ in range(n)]
vi = [[0] * m for _ in range(n)]

ans = 0
cnt= 2

for i in range(n):
    for j in range(m):
        if vi[i][j] == 0:
            vi[i][j] = cnt
            BFS(i,j, cnt)
            cnt+=1


print(ans)