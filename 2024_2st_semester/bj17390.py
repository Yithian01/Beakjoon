import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ma = [0] + list(map(int, input().split()))
ma.sort()

dp = [0] * (n+1)
dp[1] = ma[1]
for i in range(2, n+1):
    dp[i] = dp[i-1] + ma[i]


for _ in range(m):
    st, ed = map(int, input().split())
    print( dp[ed] - dp[st-1])