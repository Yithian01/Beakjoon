import sys
input = sys.stdin.readline
INF = sys.maxsize
# 너무 형식적인 DP다.
# 처음과 끝을 고정하고 중간에서 DP를 찾는 것 

# RBG이기에 3번만 반복
# dp[0][j] 는 기준을 잡는 초기 값임 <--- 가장 작은 값만 찾기 떄문에 이후에 점화식이 성립함
# 1 ~ n-1까지 반복하며 j번째의 현재값과 이전 dp값들 중 가장 작은 것을 더한다,
#       이때 주의점: j번째의 0은 이전 dp의 1,2 을 1는 이전 dp의 0,2값들 중 가장 작은 값과 더해야 한다.


# 마지막과 처음은 겹치면 안되므로 dp[-1][i]는 제외하고 ans와 비교해 min값을 넣어주면 된다.
# 시간복잡도 계산: O(N^2) 정도 내부에 *3이 있지만 작으므로 생략
n = int(input())
ma = [list(map(int, input().split())) for _ in range(n)]
ans = INF
for i in range(3):
    dp = [[INF] * 3 for _ in  range(n)]
    
    dp[0][i] = ma[0][i]
    for j in range(1, n):
        dp[j][0] = ma[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = ma[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = ma[j][2] + min(dp[j-1][0], dp[j-1][1])

    for j in range(3):
        if i != j:
            ans = min(ans, dp[-1][j])

print(ans)