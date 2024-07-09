# r = 자리수, c = 숫자 
# dp[0] = 당연히 1자리수  =>  0이 될 수 없기에 dp[0][1] ~ dp[0][9] 까지 1개 초기화 
# 2자리수 부터 점화식이 들어간다.
# 끝에 자리가 0이라면 바로 앞의 숫자는 1이여야 한다.
# 끝네 자리가 9라면 바로 앞의 숫자는 8이여야한다.

# 2자리 일때 
# 끝자리가 j인 경우 계단수 
# 0 = 10 
# 1 = 21 
# 2 = 12, 32 
# 3 = 23, 43 
# 4 = 34, 54 
# 5 = 45, 65 
# 6 = 56, 76 
# 7 = 67, 87 
# 8 = 78, 98  
# 9 = 89  

import sys
input = sys.stdin.readline
MOD = 10 ** 9

n = int(input())
dp = [[0] * 10 for _ in range(n)]

for i in range(1, 10):
    dp[0][i] = 1



for i in range(1, n):
    
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]

    for j in range(1,9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]



print(sum(dp[n-1]) % MOD)