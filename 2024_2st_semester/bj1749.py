import sys
input = sys.stdin.readline
'''

    누적합을 위해 ma의 마깥쪽을 0으로 감싸준다. ( padding 작업 )


'''
INF = -sys.maxsize

n, m = map(int, input().split())
ma = [[0 for _ in range(m+2)]]
for i in range(n):
    s = [0] + list(map(int,input().split())) + [0]
    ma.append(s)
ma.append( [0 for _ in range(m+2)])

dp = [[0] * (m+2) for _ in range(n+2)]
dp[1][1] = ma[1][1]

for i in range(2, n+1):
    dp[i][1] = dp[i-1][1] + ma[i][1]
for j in range(2, m+1):
    dp[1][j] = dp[1][j-1] + ma[1][j]


for i in range(2, n+1):
    for j in range(2, m+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + ma[i][j]

ans = INF
for sr in range(1, n+1):
    for sc in range(1, m+1): # 시작

        for er in range(sr, n+1):
            for ec in range(sc, m+1): # 끝점
                tmp = dp[er][ec] - dp[er][sc-1] - dp[sr-1][ec] + dp[sr-1][sc-1]
                ans = max(ans, tmp)


print(ans)