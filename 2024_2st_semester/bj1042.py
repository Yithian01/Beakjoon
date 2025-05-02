from collections import deque
import sys
input = sys.stdin.readline
dir = [[0, 1, 3],
       [1, 0, 2, 4],
       [2, 1, 5],
       [3, 0, 4, 6],
       [4, 1, 3, 5, 7],
       [5, 2, 4, 8],
       [6, 3, 7],
       [7, 4, 6, 8],
       [8, 5, 7]]

'''

'''


for _ in range(int(input())):
    vi = [False] * (1 << 9) # 0 ~ (1 << 9) - 1 이다.

    q = deque()

    tmp = 0
    cnt = 0
    for i in range(3):
        s = input().rstrip()
        for j, val in enumerate(s):
            if val == '*':
                tmp += (1 << cnt)

            cnt += 1

    vi[tmp] = True
    q.append((0, tmp))
    ans = 0
    while q:
        

        cw, cn = q.popleft()
        if cn == 0:
            ans = cw
            break


        for i in range(9):
            nn = cn
            

            for dn in dir[i]:
                nn ^= (1 << dn)
        
            if not vi[nn]:
                vi[nn] = True
                q.append((cw +1, nn))

    
    print(ans)