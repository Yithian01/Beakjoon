from collections import deque
import sys
input = sys.stdin.readline
dir = [(-1, 0),(1, 0),(0, -1),(0, 1)]

def BFS(r, c):
    q = deque()
    q.append((r,c))
    res = 1

    while q:
        cr, cc = q.popleft()

        for dr, dc in dir:
            nr = cr + dr 
            nc = cc + dc

            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue

            if vi[nr][nc] or ma[cr][cc] != ma[nr][nc]:
                continue


            vi[nr][nc] = True
            q.append((nr,nc))
            res +=1

    return res

def convert(r, c, cnt):
    q = deque()
    q.append((r,c))
    ma[i][j] = li[r][c]

    while q:
        cr, cc = q.popleft()

        for dr, dc in dir:
            nr = cr + dr 
            nc = cc + dc

            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue

            if vi[nr][nc] or ma[nr][nc] != cnt:
                continue

            vi[nr][nc] = True
            ma[nr][nc] = li[r][c]
            q.append((nr,nc))



n, m = map(int, input().split())

ma = [list(map(int, input().split())) for _ in range(n)]
li = [list(map(int, input().split())) for _ in range(n)]

vi = [[False] * m for _ in range(n)]
# (1) 개수 동일해야 함 --> 숫자가 바뀌어서 다른 곳과 합쳐질 수도 있음 
# (2) 바뀌는 곳은 한곳이어야한다. 2군데 이상 바뀌는 곳도 체크해주어야 한다.
# 전과 달라진 곳이 한개라도 나온다면 넣고 돌리자, 후과 달라진 곳이 있으면 불통과 

isChange = False
for i in range(n):
    for j in range(m):
        if ma[i][j] != li[i][j] and  not isChange:
            isChange = True
            vi[i][j] = True
            convert(i, j, ma[i][j]) # 바뀌어야 할 숫자


ans = False
for i in range(n):
    for j in range(m):
        if ma[i][j] != li[i][j]:
            ans = True
            break
    if ans:
        break

if ans:
    print(f'NO')
else:
    print("YES")