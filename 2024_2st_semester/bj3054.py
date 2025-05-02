import sys
input = sys.stdin.readline
dir = [(-2, 0),  (2, 0), 
       (-1, -1), (-1, 1),
       (1, -1),  (1, 1),
       (0, -2),  (0, 2) ]


'''
    가로의 길이 = (n * 5) - (n - 1)

'''

s = input().rstrip()
m = ( (len(s) * 5) - (len(s) - 1) )
ma = [['.'] * m for _ in range(5)]

cnt = 1
for i in range(2, m, 4):
    ma[2][i] = s[cnt-1]

    for dr ,dc in dir:
        nr = 2 + dr 
        nc = i + dc 


        
        if cnt % 3 == 0:
            ma[nr][nc] = '*'
        else:
            if cnt != 1 and (cnt-1) % 3 == 0  and dc == -2:
                ma[nr][nc] = '*'
            else:
                ma[nr][nc] = '#'
        
    cnt += 1

for i in range(5):
    for j in range(m):
        print(ma[i][j], end= '')
    print()