from collections import deque
import sys
input = sys.stdin.readline
dir = [(-1,0),(1,0),(0,-1),(0,1)]
INF = 2e9 

ma = [[0] * (501) for _ in range(501)]
vi = [[INF] * (501) for _ in range(501)]

for _ in range(int(input())):
    sr, sc, er, ec = map(int,input().split())   
    if er < sr :
        sr, er = er, sr
    if ec < sc :
        sc, ec = ec, sc


    for i in range(sr , er + 1):
        for j in range(sc, ec + 1):
            ma[i][j] = 1


for _ in range(int(input())):
    sr, sc, er, ec = map(int,input().split())   
    if er < sr :
        sr, er = er, sr
    if ec < sc :
        sc, ec = ec, sc


    for i in range(sr , er + 1):
        for j in range(sc, ec + 1):
            ma[i][j] = 2
vi[0][0] = 0



if ma[500][500] == 2:
    print(-1)
    exit(0)

q = deque()
q.append((0, 0))
while q:
    
    r, c = q.popleft()
    for dr, dc in dir:
        nr = r + dr 
        nc = c + dc

        if nr < 0 or nr >= 501 or nc < 0 or nc >= 501:
            continue

        if ma[nr][nc] == 2:
            continue

        tmp = 0 
        if ma[nr][nc] == 1:
            tmp = 1

        if vi[nr][nc] > vi[r][c] + tmp:
            vi[nr][nc] = vi[r][c] + tmp
            q.append((nr,nc))


if vi[500][500] == INF:
    print(-1)
else:
    print(vi[500][500])