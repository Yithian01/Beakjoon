import sys
input = sys.stdin.readline


n, m = map(int, input().split())
ma = list(map(int, input().split()))
dp = [0] * (n+1)

for i in range(n):
    if ma[i] % 2 == 0:
        dp[i+1] = dp[i] + 1
    else:
        dp[i+1] = 0



print(f' dp = {dp}')