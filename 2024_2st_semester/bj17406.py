from itertools import permutations
import sys, copy
input = sys.stdin.readline
dir = [1, 1 , -1, -1]
INF = sys.maxsize


# def sol(sr, sc, er, ec, cd):
#     global ma    

#     for i in range(sr, er):
#         for j in range(sc, ec):
#             nr = i + dir[cd][0]
#             nc = j + dir[cd][1]

#             if i == er -1 and j == ec - 1:


n, m, k = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]

q = []
for _ in range(k):
    r, c, s = map(int, input().split())
    r, c = r-1, c-1
    q.append((r,c,s))


ans = INF
for per in permutations(q):
    ma = copy.deepcopy(li)

    for pe in per:
        dp = copy.deepcopy(ma)
        r, c, s = pe

        for i in range(1, s + 1):
            tco = []
            tco.append(dp[r-i][c+i] )
            tco.append(dp[r+i][c+i] )
            tco.append(dp[r+i][c-i])

            for j in range(c-i, c+i):
                nc = j + dir[0]
                ma[r-i][nc] = dp[r-i][j]

            for j in range(r-i+1, r+i):
                nr = j + dir[1]
                ma[nr][c+i] = dp[j][c+i]
            ma[r-i+1][c+i] = tco[0]

            

            for j in range(c+i-1, c-i, -1):
                nc = j + dir[2]
                ma[r+i][nc] = dp[r+i][j]
            ma[r+i][c+i-1] = tco[1]


            
            for j in range(r+i-1, r-i, -1):
                nr = j + dir[3]
                ma[nr][c-i] = dp[j][c-i]
            ma[r+i-1][c-i] = tco[2]

    for i in range(n):
        ans = min(ans, sum(ma[i]))
    
        
print(ans)