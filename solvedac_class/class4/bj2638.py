# 공기 = 0, 치즈 = 1, 치즈안에 공기 = ??
# 1) bfs 할때 공기면 q에 append 치즈라면 방문여부 + 1
# 2) 이렇게 하면 vi배열에는 공기 = 1, 치즈 >= 1, 치즈안에 공기 = 0
# 3) 그리고 2이상인 치즈가 외부에 노출되는 치즈이다.
# 4) (3)인 부분을 0으로 바꿔주고 모든 공간이 0일 때까지 반복 

# 시간 복잡도계산 : ( bfs + 확인 ) * X => X = ??
#                 가장자리는 모두 비어있다는 가정이 있음 
#                 98 * 98 // 2 정도가 한번에 벗겨지는 최소항일 것임 
#                 98번 반복한다면 10^2 정도를 반복 

#                 총 NM * N => 10^4 * 10^2 => 10^6
from collections import deque
import sys
input = sys.stdin.readline
dir = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs(r, c):
    q = deque()
    q.append((r,c))
    vi[r][c] = 1

    while q:
        r, c = q.popleft()
        for dr, dc in dir:
            nr = r + dr 
            nc = c + dc 

            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue

            if vi[nr][nc] == 0 and ma[nr][nc] == 0:
                vi[nr][nc] = 1
                q.append((nr,nc))

            elif ma[nr][nc] == 1:
                vi[nr][nc] +=1
            

n, m = map(int, input().split())
ma = [list(map(int ,input().split())) for _ in range(n)]

ans = 0
while True:
    vi = [[0] * m for _ in range(n)]
    bfs(0,0)

    ans += 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if vi[i][j] >= 2:
                ma[i][j] = 0

            if ma[i][j] == 1:
                cnt +=1
            

    if cnt == 0:
        break


print(ans)