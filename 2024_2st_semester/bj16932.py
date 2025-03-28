import sys
from collections import deque
input = sys.stdin.readline
dir = [(-1, 0),(1, 0),(0, -1),(0, 1)]


'''
    한개를 1로 변경했을 때 붙어있는 최대 1크기 구하기
    n = 10^3

    1) 각 영역으로 체크 cnt를 이용해서 1인 구역들을 영역으로 숫자 체크
'''

n, m = map(int, input().split())
ma = [list(map(int, input().split())) for _ in range(n)]
vi = [[-1] * m for _ in range(n)]


def BFS(r, c, cnt):
    global vi
    q = deque()
    q.append((r,c))

    cost = 1
    vi[r][c] = cnt
    while q:
        cr, cc = q.popleft()
        
        for dr, dc in dir:
            nr = cr + dr
            nc = cc + dc 
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue

            if ma[nr][nc] == 0 or vi[nr][nc] != -1:
                continue


            vi[nr][nc] = cnt
            q.append((nr, nc))
            cost += 1

    return cost


ta = {}
res = 1
for i in range(n):
    for j in range(m):
        if ma[i][j] == 1 and vi[i][j] == -1:
            ta[res] = BFS(i, j, res )
            res += 1


ans = 0

for i in range(n):
    for j in range(m):
        tmp = set()
        if vi[i][j] == -1:
            for dr, dc in dir:
                nr = i + dr 
                nc = j + dc
                if nr < 0 or nr >= n or nc < 0 or nc >= m:
                    continue

                if vi[nr][nc] == -1:
                    continue

                tmp.add(vi[nr][nc])
                
            
            cost = 1
            for k in tmp:
                cost += ta[k]

            ans = max(ans, cost)


print(ans)