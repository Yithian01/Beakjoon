# 1) 시작점을 찾지 않고 표면을 둘러서 자동으로 찾게 하는 기법
# 2) 문을 열었다면 그 지점부터 Vi배열과, q를 다시 선언하고 그 지점부터 이어서 시작 하는 것 

# 시간 복잡도계산 : TC * NM
from collections import deque
import sys
input = sys.stdin.readline
dir = [(-1,0), (1, 0),(0, -1),(0,1)]

def BFS(r, c):
    q = deque()
    vi = [[False] * (m + 2) for _ in range(n+2)]
    q.append((r,c))
    ans = 0

    while q:
        cr, cc = q.popleft()
        for dr, dc in dir:
            nr = cr + dr 
            nc = cc + dc 
            if nr < 0 or nr >= n+2 or nc < 0 or nc >= m +2:
                continue
            
            if vi[nr][nc] or nMa[nr][nc] == '*':
                continue

            if nMa[nr][nc] =='.':
                vi[nr][nc] = True
                q.append((nr, nc))
            
            elif nMa[nr][nc].islower(): # 소문자 확인
                doorKey[ord(nMa[nr][nc]) - 97] = True
                nMa[nr][nc] = '.'
                q = deque()
                vi = [[False] * (m+2) for _ in range(n+2)]
                q.append((nr,nc))

            elif nMa[nr][nc].isupper() and doorKey[ord(nMa[nr][nc]) - 65]:
                vi[nr][nc] = True
                nMa[nr][nc] = '.'
                q.append((nr,nc))
            elif nMa[nr][nc] == '$':
                vi[nr][nc] = True
                nMa[nr][nc] = '.'
                ans += 1
                q.append((nr,nc))

    print(ans)



for _ in range(int(input())):
    n, m = map(int, input().split())
    ma = [list(input().rstrip()) for _ in range(n)]
    doorKey = [False] * 27

    s = input().rstrip()
    for i in s:
        if i == '0':
            break

        doorKey[ord(i) - 97] = True

    for i in range(n):
        for j in range(m):
            if ord('A') <= ord(ma[i][j]) <= ord('Z'):
                if doorKey[ord(ma[i][j]) - 65]:
                    ma[i][j] = '.'


    nMa = [['.'] * (m+2)]
    for i in ma:
        nMa.append(['.'] + i + ['.'])
    nMa.append(['.'] * (m+2))

    
    BFS(0,0)
