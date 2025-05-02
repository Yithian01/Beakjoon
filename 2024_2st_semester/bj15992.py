import sys
input = sys.stdin.readline
INF = 10 ** 9 + 9
'''
    성결대 컴공과 20학번 이준서가 로직 알려줌
    로직 듣고 바로 만듬 ㅅㄱ

    
    시간복잡도 : 자기 자신보다 더 많은 수로 자신을 만들 수 없다. O(NM) 정도

    시그마 정도 : n(n + 1) // 2

'''

dp = [[0] * 1001 for _ in range(1001)]
dp[1][1] = 1
dp[2][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 2
dp[3][3] = 1

for i in range(4, 1001):
    for j in range(1, i+1):
        dp[i][j] += dp[i-1][j-1] + dp[i-2][j-1] + dp[i-3][j-1]
        dp[i][j] %= INF



for _ in range(int(input())):
    n, m = map(int , input().split())
    print(dp[n][m])