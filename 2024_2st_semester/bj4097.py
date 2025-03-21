import sys
input = sys.stdin.readline
INF =  -sys.maxsize

while True:
    ma = []
    
   
    n = int(input())

    if n == 0:
        break
    
    
    for _ in range(n):
        ma.append(int(input()))

    dp = [INF] * (n+1)
    dp[0] = ma[0]

    for i in range(1, n):
        dp[i] = max(ma[i], dp[i-1] + ma[i])

    ans = INF
    for i in dp:
        ans = max(ans, i)

    print(ans)