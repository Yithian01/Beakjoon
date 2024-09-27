# 행은 A 열은 B dp[i][j]는 A가 B까지 왔을때 최장거리 
# A[i]와 B[j]가 같다면 dp[i-1][j-1] + A[i] 를 더한 값이 가장 긴 값이 확정 
# 
# 시간복잡도 계산: O(NM)
import sys
input = sys.stdin.readline

a = [""] + list(input().rstrip())
b = [""] + list(input().rstrip())
dp = [[""] * len(b) for _ in range(len(a))]

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1] + a[i]

        else:
            if len(dp[i-1][j]) >= len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            
            else:
                dp[i][j] = dp[i][j-1]


print(len(dp[-1][-1]))
print(dp[-1][-1])
                

