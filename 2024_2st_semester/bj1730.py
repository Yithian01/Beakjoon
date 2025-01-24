from collections import deque
import sys
input = sys.stdin.readline
# 시간 복잡도 : N^2 이거나 S의 길이 이거나 


dir = { 'U' : (-1, 0), 'D' : (1, 0), 'L' :(0, -1), 'R' : (0, 1), 
        (-1, 0) : 'U' ,(1, 0) : 'D', (0, -1) : 'L', (0, 1) : 'R'}
num = {0 : '.', 1 : '|', 2 : '-',  3 : '+'}
#        없음     수직      수평     둘다

n = int(input())
s = input().rstrip()
ma = [[0] * n for _ in range(n)]
isTrue = False

q = deque()
q.append( (0, 0, 0) )  # 좌표, 현재 명령 
while q:
    cr, cc, cm = q.popleft()
    if cm >= len(s):
        break

    while True:
        if cm >= len(s):
            isTrue = True
            break

        dr, dc = dir[ s[cm]]
        nr, nc = cr + dr, cc + dc

        if nr < 0 or nr >= n or nc < 0 or nc >= n:
            cm += 1
            continue
        break

    if isTrue:
        break

    # 여기까지 왔다면 갈 수 있는 곳 
    # 1. 없을 때 ( 수직, 수평)
    if dir[(dr, dc)] == 'U' or dir[(dr, dc)] == 'D':
        
        if ma[cr][cc] == 0:
            ma[cr][cc] = 1

        elif ma[cr][cc] == 2:
            ma[cr][cc] = 3
        
        if ma[nr][nc] == 0:
            ma[nr][nc] = 1

        elif ma[nr][nc] == 2:
            ma[nr][nc] = 3


    else:

        if ma[cr][cc] == 0:
            ma[cr][cc] = 2

        elif ma[cr][cc] == 1:
            ma[cr][cc] = 3
        
        if ma[nr][nc] == 0:
            ma[nr][nc] = 2

        elif ma[nr][nc] == 1:
            ma[nr][nc] = 3        
    
    q.append( (nr, nc, cm + 1))

        
    
for i in range(n):

    for j in range(n):
        print( num[ma[i][j]] , end='')
    print()

