# n-1번만큼 자리수 
#       - 각 현재 숫자를 가지고 다음 숫자로 넣어주기 때문에 n-1번 반복한다.
# 0 ~ 9까지 숫자를 사용할 수 있다.
# 그 숫자를 사용하면서 사용된 숫자를 체크한다.

# 먼저 dp[1][0 ~ 9][자기 수] <--- 1자리 수일 때 
#       1자리 수일 때 1은 1번 
#       1자리 수일 떄 2는 1번 이런식으로 정의
#       초기세팅 

# 1) 1자리 수일 때 숫자가 1인 숫자는 2자리 수일때 2인 숫자에 2와1을 가진 비트 마스킹에 +1 을 해줄 수 있다.
# (1)번 반복

# 시간복잡도 계산: 10^2 * 10 * 10 => 10^4정도
import sys
input = sys.stdin.readline
MOD = 10 ** 9

#  9876543210  <--- 사용한 숫자
# 10000000000  <--- bitMasking으로 10bit만 사용 가능함
maxLen = 1 << 10 
n = int(input())
dp = [[[0] * maxLen for _ in range(10)] for _ in range(n+1)]
#[자리수][가능한 숫자][사용한 숫자 bit]

for i in range(1, 10):
    dp[1][i][1 << i] = 1



for i in range(1, n):
    for j in range(10): # 
        for k in range(maxLen): # 사용한 숫자 bit
            
            if j > 0:
                nn = k | 1 << ( j - 1 )
                dp[i+1][j-1][nn] += dp[i][j][k]
                dp[i+1][j-1][nn] %= MOD
                

            if j < 9:
                nn = k | 1 << ( j + 1 )
                dp[i+1][j+1][nn] += dp[i][j][k]
                dp[i+1][j+1][nn] %= MOD

res = 0
for i in range(10):
    res += dp[n][i][maxLen -1]
    res %= MOD

print(res)
            