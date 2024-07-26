# 해당하는 최대 경사에 대해서 이분탐색을 통해서 logN으로 나온 값을 bfs를 사용해서 경로를 찾는다.
# 1) bfs --> 최단거리(방문체크) 하면서 경사값(mid)을 만족하는 경로가 존재한다면 True
# 2) 이분탐색  FFFFTTTTTTT  이므로 ( ] 이다. 즉 le, ri = -1, INF값

# 시간복잡도 계산: N^2 log M => 10^6 * log ( 10^9 ) --> 3 * 10^7정도
from collections import deque
import sys
input = sys.stdin.readline
INF = 10**9
dir = [(-1,0),(1,0),(0,-1),(0,1)]



def bfs(mid):
    q = deque()
    vi = [[False] * n for _ in range(n)]
    vi[0][0] = True
    q.append((0,0))

    while q:
        cr, cc = q.popleft()
        if cr == n-1 and cc == n-1:
            return True

        for dr, dc in dir:
            nr = cr + dr
            nc = cc + dc 

            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue

            if not vi[nr][nc]:
                if abs(ma[nr][nc] - ma[cr][cc]) <= mid:
                    
                    
                    vi [nr][nc] = True
                    q.append((nr,nc))


n = int(input())
ma = [list(map(int, input().split())) for _ in range(n)]
vi = [[False] * n for _ in range(n)]
vi[0][0] = True


#FFFFFTTTTTT     ( ]   
le, ri =  -1, INF
while le + 1 < ri:
    mid = (le + ri) // 2

    if bfs(mid):
        ri = mid
    else:
        le = mid
    
print(ri)