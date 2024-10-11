# dp를 사용
# dp[0][1] = AB를 한 값 
# dp[1][2] = BC를 한 값 
# dp[0][2] = 2가지 방법이 있음
# 1)  ( AB )C 
# 2)  A ( BC )
# 시작과 끝은 st, ed로 두고 어디부터 곱할지 k를 두고 결정함 

# st = 0, ed = 2일때  k = 0, 1
# k = 0일 때 (BC)를 먼저 하는 것 
# dp[0][0] + dp[1][2]  + (ma[0][0] * ma[0][1] * ma[2][1] )
# 예제로 본다면 
# A = 5x3
# B = 3x2
# C = 2x6
# 1) AB, BC의 행열곱을 구한다.
# 2) (AB)C ,    A(BC)를 구한다.

# 시간 복잡도 계산: n*n*n => O(n^3)
import sys
input = sys.stdin.readline
INF = 2e9

n = int(input())
ma = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

for st in range(n-1):
    for i in range(n - 1 - st):
        j = i + 1 + st 
        
        dp[i][j] = INF
        for k in  range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + ma[i][0] * ma[k][1] * ma[j][1])
    

print(dp[0][-1])