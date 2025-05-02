import sys
input = sys.stdin.readline
n = 5 * (10 ** 3)

m = int(input())
ma = list(map(int, input().split()))

dp = [[0] * n for _ in range(n)]
for i in range(m):
    dp[0][i] = ma[i]


for i in range(1, n):
    for j in range(m):
        a = dp[i-1][j] -1
        dp[i][j] = dp[i-1][a]


for _ in range(int(input())):
    st, ed = map(int, input().split())
    st -= 1
    ed -= 1
    print(dp[st][ed])


print()
for i in range(12):
    for j in range(m):
        print(dp[i][j] ,end=' ')
    print()