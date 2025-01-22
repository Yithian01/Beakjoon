# 가장 자리를 보며 탈출가능하다면 DFS를 불러서 다음과 같은 조건을 확인한다.
# 1) 현재에서 'U'의 위치가 'D'일 경우 <--------- 이 경우 자기는 탈출 가능한데 위에서 자신한테 오는 경우
# 2) 현재에서 'R'의 위치가 'L'일 경우 <--------- 이 경우 자기는 탈출 가능한데 오른쪽에서 자신한테 오는 경우
# 3) 현재에서 'L'의 위치가 'R'일 경우 <--------- 이 경우 자기는 탈출 가능한데 왼쪽에서 자신한테 오는 경우
# 4) 현재에서 'D'의 위치가 'U'일 경우 <--------- 이 경우 자기는 탈출 가능한데 아래쪼에서 자신한테 오는 경우

# 시간복잡도 계산 : 모든 부분을 이동할 수 도 있다. 즉 500 * 500 => 25 * 10^4 정도
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
#          U     R      D       L
dir = [(-1, 0),(0, 1),(1, 0),(0, -1)]
ta = {'U':0, 'R':1, 'D':2, 'L':3,
       0:'D', 1:'L', 2:'U', 3 : 'R'}



def checkDIR(cr, cc):

    if vi[cr][cc]:
        return 
    
    vi[cr][cc] = True

    for i in range(4):
        dr , dc = dir[i]
        nr = cr + dr 
        nc = cc + dc 

        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            continue

        
        if ma[nr][nc] == ta[i]:
            checkDIR(nr,nc)


    

n, m = map(int, input().split())
ma = [ list(map(str, input().rstrip())) for _ in range(n)]
vi = [[ False for _ in range(m)] for _ in range(n)]


for i in [0, n-1]:
    for j in [0, m-1]:

        if vi[i][j]:
            continue
        
        dr, dc = dir[ ta[ma[i][j]] ]
        nr = i + dr 
        nc = j + dc 

        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            checkDIR(i, j)



for i in [0, n-1]:
    for j in range(1, m-1):
        if vi[i][j]:
            continue


        dr, dc = dir[ ta[ma[i][j]] ]
        nr = i + dr 
        nc = j + dc 

        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            checkDIR(i, j)


for j in [0, m-1]:
    for i in range(1, n-1):

        if vi[i][j]:
            continue
        
        dr, dc = dir[ ta[ma[i][j]] ]
        nr = i + dr 
        nc = j + dc 

        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            checkDIR(i, j)

ans = 0
for i in range(n):
    for j in range(m):
        if vi[i][j] == True:
            ans += 1

print(ans)