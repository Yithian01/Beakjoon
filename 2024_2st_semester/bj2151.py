from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize
# dir = [(-1, 0),(1, 0),(0, -1),(0, 1),(-1, -1),(-1, -1), (-1, 1), (1, -1), (1, 1)]
ch = [(-1, 0),(1, 0),(0, -1),(0, 1)]

'''
    창문설치 문제 : 45도 기울어진 대각선 방향으로 설치 

    문 위치 
    바로보는 방향(벽 유무) 체크 
    
     
    45도 설치라고 하길래 대각선에 설치해야 하나 했는데 낚시였다.
    무조건 설치는 직각으로 가능 

    거울 사이에 "*" (벽) 이 있으면 안되는 예외 처리 필요 
    문에서 문으로 바로 갈 수 있는지 예외 처리 필요 
    직각으로만 이동하는 것 필수!!!

    
    시간복잡도 계산: O(NM)
    O(NM) : BFS, 다익스트라 와 같음 추가로 + 4n 문 -> 문으로 가는 추가적인 것 필요( 직각 이동 가능여부 확인 )    
    
'''


n = int(input())
ma = [[] for _ in range(n)]
vi = [[INF] * n for _ in range(n)]
st = [-1, -1]
ed = [-1, -1]


q = deque()
for i in range(n):

    s = input().rstrip()
    for j, v in enumerate(s):
        tmp = -1

        if v == '#':
            tmp = 2
            if len(q) == 0:
                tmp = -1
                st = [i, j]
                q.append((i, j, 0))
            else:
                ed = [i, j]

        elif v == '!':
            tmp = 1
        
        elif v == '*':
            tmp = 0

        ma[i].append(tmp)


sr, sc = st
for dr, dc in ch:
    tmp = 0

    for i in range(1, n):

        nr = sr + (dr * i)
        nc = sc + (dc * i)

        if nr < 0 or nr >= n or nc < 0 or nc >= n:
            continue

        if ma[nr][nc] == 0:
            tmp += 1
            break

        if tmp == 0 and ma[nr][nc] == 2:
            print(0)
            exit(0)
            break

     
ans = INF


while q:

    cr, cc, cw = q.popleft()

    for dr, dc  in ch:
        for cnt in range(1, n):

            nr, nc = cr + (cnt * dr) , cc + (cnt * dc)

            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue
            
            if ma[nr][nc] == 0:
                break

            if nr == ed[0] and nc == ed[1]:
                if cw > 0:
                    ans = min(ans, cw)


            if ma[nr][nc] == 1 and vi[nr][nc] > cw + 1:

                vi[nr][nc] = cw + 1
                q.append((nr,nc, cw + 1))


print(ans)