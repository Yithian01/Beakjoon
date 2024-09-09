from collections import deque
import sys
input = sys.stdin.readline
dir = [(-1, 0),(1, 0),(0, -1),(0, 1)]



wolf = []
q = deque()
n, m = map(int, input().split())
ma = [[] for _ in range(n)]
vi = [[False] * m for _ in range(n)]

for i in range(n):
    s = input().rstrip()

    for j in range(m):
        if s[j] == '#':
            ma[i].append(1)
        elif s[j] == 'W':
            q.append((i,j))
            wolf.append((i,j))
            vi[i][j] = True
            ma[i].append(0)

        elif s[j] =='+':
            ma[i].append(2)

        else:
            ma[i].append(0)


while q:
    cr, cc = q.popleft()

    for dr, dc in dir:
        nr = cr + dr 
        nc = cc + dc

        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            continue

        if vi[nr][nc] or ma[nr][nc] == 1:
            continue


        if ma[nr][nc] == 0:
            vi[nr][nc] = True
            q.append((nr,nc))

        elif ma[nr][nc] == 2:
            while True:
                if nr < 0 or nr >= n or nc < 0 or nc >= m or (ma[nr][nc] == 1 or ma[nr][nc] == 0):
                    if ma[nr][nc] == 1:
                        nr -= dr
                        nc -= dc
                    
                    break

                nr += dr 
                nc += dc

            if not vi[nr][nc]:
                vi[nr][nc] = True
                q.append((nr, nc))

            


for i in range(n):
    for j in range(m):
        if (i,j) in wolf:
            print('W', end='')
        elif ma[i][j] == 1:
            print('#', end='')
        elif ma[i][j] == 2:
            print('+', end='')
        elif ma[i][j] == 0:
            if vi[i][j]:
                print('.', end='')
            else:
                print('P', end='')

    print()


            