from collections import deque
import sys
input = sys.stdin.readline
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def BFS(r, c, w):
    q = deque()
    vi = [[False] * m for _ in range(n)]
    vi[r][c] = True

    q.append((r,c, 1, w))  # 좌표, 길이, 시작
    res = 0
    tmp = 0

    while q:
        cr, cc, cl, st= q.popleft()
        
        for dr, dc in dir:
            nr = cr + dr 
            nc = cc + dc

            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue

            if ma[nr][nc] == 0:
                continue

            if vi[nr][nc]:
                continue
                
            # False고 차이가 1인 것 확정 

            if res < cl:
                res = cl
                tmp = st + ma[nr][nc]
            elif res == cl:
                tmp = max(tmp, st + ma[nr][nc])

            q.append((nr,nc, cl + 1, st))
            vi[nr][nc] = True

    return (cl, tmp)
                
            
    
n, m = map(int ,input().split())
ma = [list(map(int, input().split())) for _ in range(n)]

num = 0
ans = 0

q = deque()
for i in range(n):
    for j in range(m):
        if ma[i][j] != 0:
            tmp = BFS(i, j, ma[i][j])
            if num < tmp[0]:
                num = tmp[0]
                ans = tmp[1]
            elif num == tmp[0]:
                ans = max(ans, tmp[1])


print(ans)