from collections import deque
import sys
input = sys.stdin.readline
dir = [(3,-2),(3, 2), # 상좌, 상우
       (-3,-2),(-3,2), # 하좌, 하우
       (2,-3),(-2,-3), # 좌하, 좌상
       (2, 3),(-2,3)]  # 우하, 우상

num = [[(1,0),(2,-1)],[(1,0),(2,1)],
       [(-1,0),(-2,-1)],[(-1,0),(-2,1)],
       [(0,-1),(1,-2)],[(0,-1),(-1,-2)],
       [(0,1),(1,2)],[(0,1),(-1,2)]]
INF = 2e9



vi = [[INF] * 9 for _ in range(10)]
sr,sc = map(int,input().split())
er,ec = map(int,input().split())

q = deque()
q.append((sr,sc, 0))
vi[sr][sc] = 0

def bfs():

    while q:
        cr, cc, we = q.popleft()
        for idx, dd in enumerate(dir):
            dr, dc = dd
            nr = cr + dr 
            nc = cc + dc 

            if nr < 0 or nr >= 10 or nc < 0 or nc >= 9:
                continue

            isCheck = False
            bbr,bbc = 0,0
            for br, bc in num[idx]:
                bbr = cr + br
                bbc = cc + bc
                if  bbr < 0 or bbr >= 10 or bbc < 0 or bbc >=9:
                    continue
                
                if bbr == er and bbc == ec:
                    isCheck = True
                    break

            if isCheck :
                continue


            if nr == er and nc == ec:
                return we + 1

            if vi[nr][nc] > vi[cr][cc] + 1:
                vi[nr][nc] = vi[cr][cc] + 1
                q.append((nr, nc, we + 1))

    return -1

print(bfs())