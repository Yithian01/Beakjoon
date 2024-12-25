from collections import deque
import sys
input = sys.stdin.readline
dir = [(0,1),(1,0),(0,-1),(-1,0)]
# BFS의 레벨개념
# cnt를 for _ in range(len(q)) 밖에 둔다.
# q에 (cnt, rr, rc, br, bc) 이렇게 두면 vi체크에 어려움이 있기에 사용함 

# 시간 복잡도 계산: n = 10임    10^2 만큼의 공간에 두 구슬의 위치의 경우의 수는 (nm)^2이다. 또한 각자 4방향으로 이동할 수 있으므로 
#                               O( (NM)^2 * 4) 정도
n, m = map(int, input().split())
ma = [list(input().rstrip()) for _ in range(n)]


red = [0, 0]
blue = [0, 0]
for i in range(n):
    for j in range(m):
        if ma[i][j] == 'R':
            red = [i, j]

        elif ma[i][j] == 'B':
            blue = [i,j]

cnt = 0
q = deque()
vi = set()
q.append((red[0], red[1], blue[0], blue[1]))
vi.add((red[0], red[1], blue[0], blue[1]))
while q:
    for _ in range(len(q)):
        rr, rc, br, bc = q.popleft()
        if cnt > 10:
            break

        if ma[rr][rc] == 'O':
            print(cnt)
            exit(0)

        for dr, dc in dir:
            nrr, nrc = rr, rc 
            while True:
                nrr += dr 
                nrc += dc 
                if ma[nrr][nrc] == '#':
                    nrr -= dr 
                    nrc -= dc 
                    break
                    
                elif ma[nrr][nrc] == 'O':
                    break
            
            nbr, nbc = br, bc 
            while True:
                nbr += dr 
                nbc += dc 
                if ma[nbr][nbc] == '#':
                    nbr -= dr 
                    nbc -= dc 
                    break
                    
                elif ma[nbr][nbc] == 'O':
                    break
                    
            if ma[nbr][nbc] == 'O':
                continue

            if nrr == nbr and nrc == nbc:
                if abs(nrr - rr) + abs(nrc - rc) > abs(nbr - br) + abs(nbc - bc):
                    nrr -= dr 
                    nrc -= dc 
                else:
                    nbr -= dr 
                    nbc -= dc 
            
            if (nrr, nrc, nbr, nbc) not in vi:
                vi.add((nrr, nrc, nbr, nbc))
                q.append((nrr, nrc, nbr, nbc))

    cnt += 1
    

print(-1)