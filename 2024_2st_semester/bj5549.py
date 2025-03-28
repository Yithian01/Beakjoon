import sys
input = sys.stdin.readline
''' 
    n*m 을 k번 에 따라 모두 반복하면 최악의 경우 nmk = 10^11이 나오므로 불가능
    즉 미리 각 칸에 대해 누적합을 해놓고 대기해야 할 듯 
    
    겉을 0으로 감싸주고 1부터 시작하는 방법을 적용하겠다.

    세로 누적합 --> 가로 누적합 후 범위 찾기 
    DP[ER][EC] - DP[ER][EC -1] - DP[SR-1][EC] + DP[SR-1][SC-1]
'''

n, m = map(int, input().split())
num = int(input())
ma = [[] for _ in range(n+2)]

for i in range(1, n+1):
    ma[i].append(0)
    for s in input().rstrip():
        ma[i].append(s)
    ma[i].append(0)
    

dp = [ list([0]* 3 for _ in range(m+2)) for _ in range(n+2)]
for i in range(1, n+1):
    for j in range(1, m+1):
        if ma[i][j] == 'J':
            dp[i][j][0] = 1
        elif ma[i][j] == 'O':
            dp[i][j][1] = 1
        elif ma[i][j] == 'I':
            dp[i][j][2] = 1



# 가로 DP 시작
for i in range(1, n+1):
    for j in range(1, m+1):
        for k in range(3):
            dp[i][j][k] += dp[i][j-1][k]

# 세로 DP 시작 
for j in range(1, m+1):
    for i in range(1, n+1):
        for k in range(3):
            dp[i][j][k] += dp[i-1][j][k]


for _ in range(num):
    sr, sc, er, ec = map(int, input().split())
    ans = [0] * 3
    for k in range(3):
        ans[k] = dp[er][ec][k] - dp[er][sc-1][k] -dp[sr-1][ec][k] + dp[sr-1][sc-1][k]

    print(*ans)

