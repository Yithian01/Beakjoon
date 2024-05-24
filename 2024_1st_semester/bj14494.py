import sys
input = sys.stdin.readline
INF =  (10 ** 9) + 7


n, m = map(int, input().split())
dp = [[0] * m for _ in range(n)]

if n == 1 and m == 1:
    print('1')
    exit(0)


for i in range(1, n):
    dp[i][0] = 1

for j in range(1, m):
    dp[0][j] = 1


dp[0][0] = 1
for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j] + dp[i][j-1]) % INF



print(dp[-1][-1])         

