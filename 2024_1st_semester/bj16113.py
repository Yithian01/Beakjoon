from collections import deque
import sys
input = sys.stdin.readline
dir = [(-1,0 ),(1, 0),(0, -1),(0, 1)]

table = {'5': '1', '7': '7', '9' : '4', '11' : '0', '12' : '0',  '13' : '8' }


def bfs(r,c ):
    q = deque()
    q.append((r,c))
    cnt = 1

    while q:
        
        cr, cc = q.popleft()
        for dr, dc in dir:
            nr = cr + dr 
            nc = cc + dc
            if nr < 0 or nr >= 5 or nc < 0 or nc >= m:
                continue

            if not vi[nr][nc] and ma[nr][nc] == '#':
                vi[nr][nc] = True
                q.append((nr,nc))
                cnt += 1

    return cnt




n = int(input())
m = n // 5
ss = input().rstrip()

ma = [ss[i : i + m] for i in range(0, n, m)]
vi =   [[False] * m for _ in range(5)]
ans = []
for i in range(m):
    if not vi[0][i] and ma[0][i] == '#':
        vi[0][i] = True
        
        cnt = bfs(0, i)
        if cnt == 11: 
            if vi[1][i] == True and vi[3][i+2] == True:
                ans.append('5')
            elif vi[1][i+2] == True and vi[3][i] == True:
                ans.append('2')
            else:
                ans.append('3')

        elif cnt == 12: 
            if vi[1][i+2] == True and vi[3][i] == True:
                ans.append('0')
            elif vi[1][i+2] == False:
                ans.append('6')
            else:
                ans.append('9')

        else:
            ans.append(table[str(cnt)])


print(''.join(ans))
