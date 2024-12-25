import sys
input = sys.stdin.readline
# dp를 사용 3차원 배열 
# dp[i][j][k] ==> i=현재 진행 사항, j = 왼쪽발위치, k = 오른발위치 
# dp[0][0][0] => 0번 까지 진행했을 때 왼발이 0에 오른발이 0에 있을 때의 최소값 
# 
# 점화식 => 3중 for문을 두었을 때 dp[i][j][k]는 이전의 위치를 나타냄 
# dp[i + 1][j][po] = 다음 위치로 오른발을 이동시킴 ,  po = ma[i]를 나타냄 
# min값 => dp[i+1][j][po], dp[i][j][k] + nextPo(k, po)    ,    k --> po로 이동하는 값을 
# 현재까지 진행했을 때 왼발, 오른발의 값 => 이 값은 이전 값들의 결과에 의한 최소값임 
# 이전최소값에서 오른발을 진행했을 떄의 값 => 이 값은 이제 움직여보려는 값임 

# 시간복잡도 계산: n * 5 * 5
INF = 10 ** 8 

ma = list(map(int, input().split()))
dp = [[[INF for _ in range(5)]for _ in range(5)] for _ in range(len(ma))]
dp[0][0][0] = 0

def nextPo(cr, nr):
    if cr == 0:
        return 2
    elif cr == nr:
        return 1
    elif abs(cr - nr) == 2:
        return 4
    else:
        return 3
    
for i in range(len(ma)-1):
    tmp = ma[i]
    for j in range(5):
        for k in range(5):
            dp[i+1][j][tmp] = min(dp[i+1][j][tmp], dp[i][j][k] + nextPo(k, tmp))
            dp[i+1][tmp][k] = min(dp[i+1][tmp][k], dp[i][j][k] + nextPo(j, tmp))


ans = INF
for i in range(5):
    for j in range(5):
        ans = min(ans, dp[len(ma)-1][i][j])

print(ans)