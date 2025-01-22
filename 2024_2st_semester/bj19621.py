from collections import deque
import sys
input = sys.stdin.readline

# 개수를 구하는 그리디가 아닌 dp도 안된다. 2^31 * 25 = 10^10정도라서 1초를 벗어난다.
# 자신의 +-1과는 함께할 수 없다는 규칙이 있었다. 그러므로 가능한 경우의 수 역시 줄어든다.
#시간 복잡도 계산: 



ans = 0
n = int(input())
ma = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n+1)
dp[1] = ma[0][2]

for i in range(2, n+1):
    ans = 0
    for j in range(0, i-1):
        ans = max(ans, (dp[j] + ma[i-1][2]))

    dp[i] = max(dp[i-1], ans)

print(dp[-1])     
    