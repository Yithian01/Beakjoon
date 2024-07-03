# dp풀이법 
# i를 기준으로 0 ~ i까지 j로 표시하며 체크
# j ~~ i 라고 생각하면 편하다.
# j ~~ i 사이를 고려하기 위해서는 i - j 가 2보다 클때 ma[j+1][i-1]이 1인지 비교한다.
# ma[j+1][i-1] 은 j+1과 i-1이 똑같은가 확인하는 부분
#
#
# 시간 복잡도 계산: 25*10^2 * 25*10^2 => 6*10^6
import sys
input = sys.stdin.readline
INF = 1e9

s = input().rstrip()
n = len(s)

ma = [[0] * n for _ in range(n)]
dp = [INF] * (n+1)
dp[n] = 0

for i in range(n):
    for j in range(i+1):    
        if s[i] == s[j] and (i - j < 2 or ma[j+1][i-1] == 1):
            ma[j][i] = 1
            dp[i] = min(dp[i], dp[j-1] + 1)

print(dp[n-1])
