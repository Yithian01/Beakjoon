from collections import deque
import sys
input = sys.stdin.readline
# BFS 자리마다 vi를 새로 만드는 방식은 불가능하다.
# (10^3)^3 이기에 불가능 하다. <-- 정답은 찾지만 시간내에 불가능 

# 1) 벽이 아닌 곳을 먼저 탐색해서 각 구역의 숫자를 만들고 그 구역의 크기를 ta에 넣는다.
# 2) 벽인 곳을 찾아서 자신의 4방향에서 ta에 들어있는 구역을 겹치지 않게 그 값에 +1한다.
# 시간 복잡도 : 빈공간BFS + 벽위치4방향탐색( 이때 중복되어있는지 추가적으로 확인 )
# 10^6 + 10^6 * 4 * k => O(4NMk) 
dir = [(-1, 0),(1, 0),(0, -1),(0, 1)]
n, m = map(int, input().split())
ma = [list(map(int, input().rstrip())) for _ in range(n)]
vi = [[0] * m for _ in range(n)]
ans = [[0] * m for _ in range(n)]
ta = {}

def BFS(r, c, t):
    q = deque()
    q.append((r,c ))
    vi[r][c] = t
    cnt = 1

    while q:
        cr, cc = q.popleft()
        
        for dr, dc in dir:
            nr = cr + dr
            nc = cc + dc 

            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue

            if vi[nr][nc] != 0:
                continue
        
            if ma[nr][nc] == 0:
                cnt += 1
                vi[nr][nc] = t
                q.append((nr,nc))
    
    return cnt 


cnt = 1
for i in range(n):
    for j in range(m):
        if ma[i][j] == 0 and vi[i][j] == 0:
            ta[cnt] = BFS(i, j, cnt)
            cnt += 1

for i in range(n):
    for j in range(m):
        if ma[i][j] == 1:
            tmp = []
            num = 1
            for dr, dc in dir:
                nr = i + dr 
                nc = j + dc 

                if nr < 0 or nr >= n or nc < 0 or nc >= m:
                    continue
                
                if vi[nr][nc] == 0:
                    continue

                if vi[nr][nc] not in tmp:
                    tmp.append(vi[nr][nc])
                    num += ta[vi[nr][nc]]

            ans[i][j] = num % 10
                      
                

for i in range(n):
    print(*ans[i], sep='')