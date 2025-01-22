import sys
input = sys.stdin.readline

def catch(x):
    cnt = 0
    for i in range(n):
        if ma[i][x]:
            cnt += ma[i][x][2]
            ma[i][x] = 0
            return cnt
    
    return 0


def next():
    # 속도, 방향, 크기
    global ma 
    newMa = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if ma[i][j] == 0:
                continue

            # 좌표, 방향 = 좌표, 속도, 방향
            nr, nc, nd = nextPosition(i, j, ma[i][j][0], ma[i][j][1])

            if newMa[nr][nc] == 0 or newMa[nr][nc][2] < ma[i][j][2]: # 비어있거나, 크기 비교
                newMa[nr][nc] = (ma[i][j][0], nd, ma[i][j][2])

    
    ma = newMa

def nextPosition(r, c, s, d):
#   n = 4라면 0 1 2 3 2 1  로 %연산이 가능해진다.
#   n = 5라면 0 1 2 3 4 3 2 1  로 %연산이 가능해진다.
#   즉 (n-1) * 2
    if d == 1 or d == 2:
        if d == 1: # 위로 올라가려면 좌표는 - 로 해줘야 한다,
                   # 위에서 싸이클이 되려는 곳에서 - i를 해줘야 위, 아래를 알 수 있다.
            s += 2 * (n - 1) - r
        else:
            s += r 
        
        s %= (n -1 ) * 2
        if s < n:
            return (dr[s], c, 2)
        
        else:
            return (dr[s], c, 1)
    

    else:
        if d == 4:
            
            s += 2 * (m - 1) - c
        else:
            s += c
        
        s %= (m-1) * 2
        if s < m:
            return( r, dc[s], 3)
        else:
            return(r, dc[s], 4)


ans = 0
n, m, k = map(int ,input().split())
dr = [ _ for _ in range(n)]
dc = [ _ for _ in range(m)]
for i in range(n-2, 0, -1):
    dr.append(i)
for i in range(m-2, 0, -1):
    dc.append(i)

ma = [[0] * m for _ in range(n)]


for i in range(k):
    r, c, s, d, z = map(int, input().split())
    r -= 1 
    c -= 1
    ma[r][c] = (s, d, z)  

for j in range(m):
    ans += catch(j)
    next()


print(ans)