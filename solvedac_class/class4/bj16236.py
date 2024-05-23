#현재 위치에서 먹을 수 있는 물고기를 다익스트라로 알아낸다. ( 시간 , 좌표)
# 못 먹는 거 나올 때까지 반복

# 시간 복잡도 계산 : 20 * 20 => 4 * 10^2  + 400 -> BFS 1번
#                   2 * 10^3 + 4 * 10^2 => 8 * 10^5
from collections import deque
n = int(input())
ma = [list(map(int, input().split()))for _ in range(n)]

dir = [(-1, 0),(0,-1),(1, 0),(0, 1)]


sr, sc = 0, 0
for i in range(n):
    for j in range(n):
        if ma[i][j] == 9:
            sr, sc = i,j


cnt = 0


def bfs(r,c):
    vi = [[0] * n for _ in range(n)]
    vi[r][c] = 0
    q = deque()
    q.append([r,c])
    fish = []
    
    while q:
        cr, cc = q.popleft()
        
        for dr, dc in dir:
            nr, nc = cr + dr, cc + dc

            if nr < 0 or nr >= n or nc < 0 or nc >= n or vi[nr][nc] != 0:
                continue

            if ma[r][c] > ma[nr][nc] and ma[nr][nc] != 0: # 먹을 수 있는 물고기 
                vi[nr][nc] = vi[cr][cc] + 1
                fish.append((vi[nr][nc] , nr,nc))        

            elif ma[r][c] == ma[nr][nc]: # 먹을 수 없는 고기
                vi[nr][nc] = vi[cr][cc] + 1
                q.append([nr,nc])
            
            elif ma[nr][nc] == 0:
                vi[nr][nc] = vi[cr][cc] + 1 # 빈 공간 
                q.append([nr,nc])



    return sorted(fish, key=lambda x : (x[0], x[1], x[2]))



cr, cc = sr, sc
size = [2, 0]
while True:
    ma[cr][cc] = size[0]
    fish = deque(bfs(cr, cc))
    
    if not fish:
        break

    we, nr, nc = fish.popleft()
    cnt += we
    size[1] += 1

    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0

    
    ma[cr][cc] = 0
    cr, cc = nr, nc

print(cnt)