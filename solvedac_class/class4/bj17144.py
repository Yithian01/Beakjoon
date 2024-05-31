# 확산, 위, 아래 로직을 구현해서 t만큼 반복한다.
# 확산 -> 4nm + nm => 4 * 6 * 50  + 300 => 4 * 3 * 10^2 + 3 * 10^ 2 => 1 * 10^3
# 위 => 2m + 2n -1 => 100 + 12 -1 => 10^2 
# 아래 => 위와 동일 

# 시간 복잡도 계산 : 10^3 * (10^3 + 10^2) => 10^6정도 
import sys
input = sys.stdin.readline
dir = [(-1,0),(1, 0),(0,-1),(0,1)]


n, m, t = map(int, input().split())
ma = [list(map(int, input().split())) for _ in range(n)]

up, down = -1, -1

for i in range(n):
    if ma[i][0] == -1:
        up = i
        down = i + 1
        break


def spread():

    tmp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if ma[i][j] != 0 and ma[i][j] != -1:
                cnt = 0
                for dr, dc in dir:
                    nr = i + dr
                    nc = j + dc

                    if nr < 0 or nr >= n or nc < 0 or nc >= m:
                        continue
                    if ma[nr][nc] == -1:
                        continue

                    tmp[nr][nc] += ma[i][j] // 5
                    cnt += ma[i][j] // 5
            
                ma[i][j] -= cnt

    for i in range(n):
        for j in range(m):
            ma[i][j] += tmp[i][j]


def upAir():
    dir = [(0, 1),(-1, 0),(0, -1),(1, 0)]
    tmp = 0 # 방향을 나타냄 (우측, 위, 좌, 아래 )
    bf = 0 
    r, c = up, 1
    
    while True:
        if r  == up and c == 0:
            break  # 공기 청정기를 만난다는 것은 한바퀴 돌았다는 것


        nr = r + dir[tmp][0]
        nc = c + dir[tmp][1]
        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            tmp += 1  ## 벽을 만나면 방향을 전환함
            continue

        ma[r][c], bf = bf, ma[r][c] # 현재 위치는 이전의 값으로 바뀜 ( 한 칸씩 민다고 생각하면 됌 )
        r, c = nr, nc


    
    
    
def downAir():
    dir = [(0, 1),(1, 0),(0, -1),(-1, 0)]
    tmp = 0 # 방향을 나타냄 (우측, 아래, 좌, 위)
    bf = 0 
    r, c = down, 1
    
    while True:
        
        nr = r + dir[tmp][0]
        nc = c + dir[tmp][1]
        if r  == down and c == 0:
            break  # 공기 청정기를 만난다는 것은 한바퀴 돌았다는 것

        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            tmp += 1  ## 벽을 만나면 방향을 전환함
            continue

        ma[r][c], bf = bf, ma[r][c] # 현재 위치는 이전의 값으로 바뀜 ( 한 칸씩 민다고 생각하면 됌 )
        r, c = nr, nc


for _ in range(t):
    spread()
    upAir()
    downAir()



ans = 0
for i in range(n):
    for j in range(m):
        if ma[i][j] != -1:
            ans += ma[i][j]
       
print(ans)