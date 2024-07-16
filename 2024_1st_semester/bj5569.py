from collections import deque
import sys
input = sys.stdin.readline
MOD = 10 **5
# 동, 북 으로만 가능
n, m = map(int, input().split())
vi = [[0] * m for _ in range(n)]
vi[1][0] = 1
vi[0][1] = 1

q = deque()
q.append((0, 1, 1, 0)) # 갈수있는방향, 가는방향, 행, 열
q.append((0, 2, 0, 1)) # 갈수있는방향, 가는방향, 행, 열
while q:
    cv, way, cr, cc = q.popleft()
    
    if cv == 1 and cr != n-1 : 
        nr, nc = cr + 1, cc + 0
        vi[nr][nc] += 1
        vi[nr][nc] %= MOD
        q.append((0, 1, nr, nc))

    if cv == 2 and cc != m-1:
        nr, nc = cr + 0, cc + 1
        vi[nr][nc] += 1
        vi[nr][nc] %= MOD
        q.append((0, 2, nr, nc))


    if cv == 0:
        if way == 1: # 위에서 온상황
            # 계속 아래로, 방향 틀기       
            nr, nc = cr + 1, cc + 0 
            if nr < n:
                vi[nr][nc] += 1
                vi[nr][nc] %= MOD
                q.append((0, 1, nr, nc))
            
            nr, nc = cr + 0, cc + 1 
            if nc < m: 
                vi[nr][nc] += 1
                vi[nr][nc] %= MOD
                q.append((2, 2, nr, nc))
        
        elif way == 2: # 옆에서 온상황
            # 계속 옆으로, 방향 틀기       
            nr, nc = cr + 0, cc + 1 
            if nc < m:
                vi[nr][nc] += 1
                vi[nr][nc] %= MOD
                q.append((0, 2, nr, nc))
            
            nr, nc = cr + 1, cc + 0 
            if nr < n: 
                vi[nr][nc] += 1
                vi[nr][nc] %= MOD
            
                q.append((1, 1, nr, nc))
    


print(vi[n-1][m-1] % MOD)