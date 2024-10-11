# 행이 시작 
# 열이 도착 
# 3~5열까지라면 
# dp[3][5]를 보면 된다.

import sys
input = sys.stdin.readline

n = int(input())
ma = list(map(int, input().split()))
dp = [[False] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = True
for i in range(n-1):
    if ma[i] == ma[i+1]:
        dp[i][i+1] = True
    
for dist in range(n-2):
    for i in range(n-2-dist):
        j = i + 2 + dist
        if ma[i] == ma[j] and dp[i+1][j-1]:
            dp[i][j] = True

for _ in range(int(input())):
    st, ed = map(int, input().split())
    if dp[st-1][ed-1]:
        print(1)
    else:
        print(0)
