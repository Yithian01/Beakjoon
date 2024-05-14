# 재귀를 통해 벽을 3개 세워주고 

#
# 시간복잡도 계산 : (8! - 5!) * 64 + 64 => O(NM) 
from collections import deque
import sys
input = sys.stdin.readline
dir = [(-1, 0),(1, 0),(0, -1),(0, 1)]

def infection(): # 확산 bfs 이용 
    global ans 
    vi = [[False] * m for _ in range(n)] 
    tmp = 0
    q = deque() 

    for i in range(n):
        for j in range(m):
            if ma[i][j] == 2:
                q.append((i,j))
                vi[i][j] = True

    while q:
        cr, cc = q.popleft()
        for dr, dc in dir:
            nr = cr + dr 
            nc = cc + dc
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue

            if ma[nr][nc] == 0 and not vi[nr][nc]:
                vi[nr][nc] = True
                q.append((nr,nc))

    for i in range(n):
        for j in range(m):
            if ma[i][j] == 0 and not vi[i][j] :
                tmp += 1


    ans = max(ans, tmp)



def makeWall(r, c, cnt):
    if cnt == 3:
        infection()
        return 

    for i in range(r, n):
        k = c if i == r else 0
        for j in range(k, m):
            if ma[i][j] == 0:
                ma[i][j] = 1
                makeWall(i, j, cnt + 1)
                ma[i][j] = 0



ans = 0 

n, m = map(int, input().split())
ma = [list(map(int, input().split())) for _ in range(n)]

makeWall(0,0,0)
print(ans)