import sys
input = sys.stdin.readline

n = int(input())
ma = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)]




dp[0][0][1] = 1
for i in range(2, n):
    if ma[0][i] == 0:
        dp[0][0][i] = dp[0][0][i-1]


for r in range(1, n):
    for c in range(1, n):



        #가로, 세로
        if ma[r][c] == 0:

            dp[0][r][c] = dp[0][r][c-1] + dp[1][r][c-1] 



            dp[2][r][c] = dp[2][r-1][c] + dp[1][r-1][c]


        #대각선 
        if ma[r][c] == 0 and ma[r-1][c] == 0 and ma[r][c-1] == 0 :
            dp[1][r][c] = dp[0][r-1][c-1] + dp[1][r-1][c-1] + dp[2][r-1][c-1]
        

ans = 0
ans += dp[0][n-1][n-1] + dp[1][n-1][n-1] + dp[2][n-1][n-1] 
print(ans)
            
