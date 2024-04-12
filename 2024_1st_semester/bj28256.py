from heapq import heappop, heappush
import sys
input = sys.stdin.readline
dir = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs(r,c):
    res = 1
    vi[r][c] = True
    q = []
    q.append((r,c))

    while q:
        tmp = []
        for cr, cc in q:
            
            for dr, dc in dir:
                nr = cr + dr 
                nc = cc + dc 

                if nr < 0 or nr >= 3 or nc < 0 or nc >= 3:
                    continue

                if not vi[nr][nc] and ma[nr][nc] == 'O':
                    res += 1
                    vi[nr][nc] = True
                    tmp.append((nr,nc))
                
        q = tmp
    
    return res


for _ in range(int(input())):
    ma = [input().rstrip() for _ in range(3)]
    vi = [[False] * 3 for _ in range(3) ]
    vi[1][1] = True

    num = list(map(int, input().split()))

    ans = []
    for i in range(3):
        for j in range(3):
            
            if not vi[i][j] and ma[i][j] == 'O':
                res = bfs(i,j)
                if res > 0:
                    ans.append(res)

    isCheck = False
    ans = [len(ans)] + sorted(ans)
    for i in range(len(ans)):
        if ans[i] != num[i]:
            isCheck = True
            break
    
    if isCheck:
        print(0)
    else:
        print(1)