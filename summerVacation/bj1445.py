# 예제 1의 경우 S -> F로 3칸만에 이동할 수 있음에도 
# 쓰레기 주의를 멀리 벗어나서 가는 경우를 찾아야 합니다.

# heap에 [지나가는 쓰레기, 주위 쓰레기, 위치정보]를 넣게 되면 
# 자동으로 쓰레기를 피해가는 최단 거리를 알 수 있습니다.

# 시간 복잡도 계산: O(NM) => heap을 사용하므로 N^2 log N^2 정도    
# N == M 이므로 N^2으로 계산 

from heapq import heappush, heappop
import sys
input = sys.stdin.readline
dir = [(0, 1),(1, 0),(0, -1),(-1, 0)]

def isGo(r, c): # 지나갈 수 있는지 체크
    
    if r < 0 or r >= n or c < 0 or c >= m:
        return False

    return True


def isNear(r,c):  # 주위 쓰레기 체크 
    
    for dr, dc in dir:
        nr = r + dr 
        nc = c + dc 

        if isGo(nr, nc) and ma[nr][nc] == 'g':
            return 1 # 하나라도 있으면 1 
    
    return 0 # 없으면 0 


st = [-1, -1]
ed = [-1, -1]

n, m = map(int, input().split())
ma = []
for i in range(n):
    s = input().rstrip()
    ma.append(s)
    
    for j in range(m):
        if s[j] == 'F':
            ed = [i, j]
        if s[j] == 'S':
            st = [i, j] 



q = []
heappush(q, (0, 0, st[0], st[1])) #지나가는 쓰레기, 주위 쓰레기, 위치 

vi = [[False] * m for _ in range(n)]
vi[st[0]][st[1]] = True

while q:
    pa, ne, cr, cc = heappop(q)

    if ed == [cr, cc]: # 종료 조건
        print(pa, ne)
        break


    for dr, dc in dir:
        nr = cr + dr 
        nc = cc + dc 

        if isGo(nr, nc) and not vi[nr][nc]:
            
            vi[nr][nc] = True

    
            if ma[nr][nc] == 'g': # 쓰레기 지나갈 때
                heappush(q, (pa + 1, ne, nr, nc))
            elif ma[nr][nc] == '.': # 쓰레기 주변 지나갈 때 
                heappush(q, (pa, ne + isNear(nr,nc), nr, nc) )
            else: # 아무것도 없을 때
                heappush(q, (pa, ne, nr, nc))