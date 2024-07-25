from collections import deque
import sys
input = sys.stdin.readline
dir = [(1,-1),(1,0),(1,1)]
INF = 1e9

cnt = 0
while True:
    cnt += 1
    n = int(input())
    if n == 0 :
        break

    ma = [list(map(int,input().split())) for _ in range(n)]
    dp = [[INF] * 3 for _ in range(n)]
    dp[0][1] = ma[0][1]
    dp[0][2] = min(INF, ma[0][1] + ma[0][2])
    ans = INF

    # c = 나올 수 있는 모든 경우의 수 
    # r = 각 행 
    # 즉 1,0 => 0에서 오는 0,1의 수 
    for i in range(1, n):
        dp[i][0] = min(dp[i-1][0] + ma[i][0] ,dp[i-1][1] + ma[i][0])   
        dp[i][1] = min(dp[i-1][0] + ma[i][1], dp[i-1][1] + ma[i][1])   
        dp[i][1] = min(dp[i][1], dp[i-1][2] + ma[i][1])  
        dp[i][1] = min(dp[i][1], dp[i][0] + ma[i][1]) 
        dp[i][2] = min(dp[i-1][1] + ma[i][2], dp[i-1][2] + ma[i][2])   
        dp[i][2] = min(dp[i][2], dp[i][1] + ma[i][2]) 


    print(f'{cnt}. {dp[n-1][1]}')

            

            


