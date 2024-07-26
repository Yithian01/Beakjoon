from collections import deque
import sys
input = sys.stdin.readline
dir = [(-1,0),(1,0),(0,-1),(0,1)]
res = ['3','4','5']
INF = 1e9
# 1)  식구는 2, 청국장은 3, 스시는 4, 맥앤치즈는 5이다.
# 2)  2, 3, 4, 5는 장애물이 아니므로 지나갈 수 있다. , 1은 벽
# 3)  시작점은 2의 위치이다.
# 4)  식구는 어떤 음식에 더 빨리 도착할 수 있을까?


n, m = map(int, input().split())
ma = [input().rstrip() for _ in range(n)]
vi = [[INF] * m for _ in range(n)]


ans = [0,INF]
q = deque()
for i in range(n):
    for j in range(m):
        if ma[i][j] == '2':
            q.append((i,j))
            vi[i][j] = 0
            break



while q:
    cr, cc = q.popleft()

    for dr, dc in dir:
        nr = cr + dr 
        nc = cc + dc 

        if nr < 0  or nr >= n or nc < 0 or nc >= m :
            continue

        if ma[nr][nc] == '1':
            continue


        if vi[nr][nc] > vi[cr][cc] +1:
            vi[nr][nc] = vi[cr][cc] + 1

            if ma[nr][nc] in res and ans[1] > vi[nr][nc]:
                ans = (ma[nr][nc], vi[nr][nc])
            q.append((nr,nc))


if ans[0] == 0:
    print('NIE')
else:
    print('TAK')
    print(ans[1])
