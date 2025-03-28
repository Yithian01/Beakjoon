import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize
dir = [(-1, 0),(1, 0),(0, -1),(0, 1)]


ed = (0, 0)
bios = 1 << 5
q = deque()
m, n = map(int, input().split())
ma = [[] for _ in range(n)]
cnt= 0
for i in range(n):
    s = input().rstrip()
    for j, val in enumerate(s):
        if val == 'X':
            ma[i].append(cnt)
            cnt += 1
            continue

        
        elif val == 'S' or val == 'E' or  val == '.':
            ma[i].append(-1)
            if val == 'S':
                q.append((i, j, 0, 0))
            elif val == 'E':
                ed = (i, j)

        else:
            ma[i].append(-2)


dp = [[[INF] * bios for _ in range(m)] for _ in range(n)]
dp[q[0][0]][q[0][1]][q[0][2]] = 0


while q:

    # 현재 좌표, 현재 방문, 현재 값
    cr, cc, cv, cw = q.popleft()

    for dr, dc in dir:
        nr = cr + dr 
        nc = cc + dc 

        if nr < 0 or nr >= n or nc < 0 or nc >= m or ma[nr][nc] == -2:
            continue

        nv = cv
        if ma[nr][nc] != -1:
            nv = nv | (1 << ma[nr][nc])

        if dp[nr][nc][nv] > cw + 1:
            dp[nr][nc][nv] = cw + 1
            q.append((nr,nc, nv, cw + 1))


ans = 0
for i in range(cnt):
    ans |= (1 << i)

print(dp[ed[0]][ed[1]][ans])