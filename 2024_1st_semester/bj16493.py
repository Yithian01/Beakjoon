import sys
input = sys.stdin.readline

n, m = map(int, input().split())
q = [(-1,-1)]
for _ in range(m):
    a, b = map(int, input().split())
    q.append((a,b))

q.sort()
dp = [[0] * (n+1) for _ in range(m+1)]

# 일수, 페이지
for i in range(1, m+1): # <--- 책정보(일수, 페이지)
    for j in range(1, n+1): # <--- 일수

        if 0 <= j - q[i][0]:
            dp[i][j] = max(dp[i][j], dp[i-1][j- q[i][0]] + q[i][1])

        dp[i][j] = max(dp[i][j], dp[i-1][j])
        dp[i][j] = max(dp[i][j], dp[i][j-1])
        


print(dp[m][n])