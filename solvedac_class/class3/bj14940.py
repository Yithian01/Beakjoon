'''주소 : https://www.acmicpc.net/problem/14940'''
import sys
input = sys.stdin.readline
INF = 2e9
dir = [(-1, 0),(1, 0),(0, -1),(0, 1)]

n, m = map(int, input().split())
ma = [list(map(int,input().split())) for _ in range(n)]
vi = [[INF] * m for _ in range(n)]


q = []
for i in range(n):
    for j in range(m):
        if ma[i][j] == 2:
            q.append((i, j))
            vi[i][j] = 0


while q:
    tmp = []
    for cr, cc in q:

        for dr, dc in dir:
            nr = cr + dr 
            nc = cc + dc

            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            
            if ma[nr][nc] == 1 and vi[nr][nc] > vi[cr][cc] + 1:
                vi[nr][nc] = vi[cr][cc] + 1

                tmp.append((nr,nc))
    q = tmp


for i in range(n):
    for j in range(m):
        if ma[i][j] == 0:
            print(0, end=' ')
        elif vi[i][j] == INF:
            print(-1, end=' ')
        else:
            print(vi[i][j], end= ' ')
    
    print()

    
