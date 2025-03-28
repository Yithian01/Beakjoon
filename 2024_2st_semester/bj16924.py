import sys
input = sys.stdin.readline
dir = [(0,1),(0,-1),(1,0),(-1,0)]

before = 0
after = 0
n, m = map(int, input().split())
ma = [[] for _ in range(n)]
for i in range(n):
    for s in input().rstrip():
        if s == '.':
            ma[i].append(0)
        elif s == '*':
            before += 1
            ma[i].append(1)
            

ans = []
vi = [[0] * m for _ in range(n)]
for i in range(1, n-1):
    for j in range(1, m-1):
        if ma[i][j] == 1:

            for k in range(1, min(n,m)):
                isTrue = False
                for dr, dc in dir:
                    nr = i + (dr * k)
                    nc = j + (dc * k)

                    if nr < 0 or nr >= n or nc < 0 or nc >= m or ma[nr][nc] == 0:
                        isTrue = True
                        break


                else:
                    vi[i][j] = 1
                    for dr, dc in dir:
                        nr = i + (dr * k)
                        nc = j + (dc * k)
                        vi[nr][nc] = 1
                    ans.append((i+1, j+1, k))
                
                if isTrue:
                    break
                    

for i in range(n):
    for j in range(m):
        if vi[i][j] >= 1:
            after += vi[i][j]


if before == after:
    print(len(ans))
    for i, j, k in ans:
        print(i, j, k)
else:
    print(-1)
