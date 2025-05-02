import sys
input = sys.stdin.readline
'''
    dp[st][ed] = st < ed일 때까지 st+1, ed-1을 한 값을 더해준다.
        ((())) = 감싸주는 경우를 구한 것 

    () + (   ),
    ( ) + (  ), 
    (  ) + ( )
    (   ) + () 인 경우 중 최고값을 구한다.

    
    시간복잡도 계산: DFS이므로  O(N^2)정도 
'''

s = input().rstrip()
n = len(s)

dp =[[-1] * n for _ in range(n)]


def DFS(st, ed):
    if st >= ed:
        return 0

    if dp[st][ed] != -1:
        return dp[st][ed]
    
    if (s[st] == 'a' and s[ed] =='t') or (s[st] == 'g' and s[ed] == "c" ):
        dp[st][ed] = DFS(st + 1, ed -1) + 2

    for i in range(st, ed):
        dp[st][ed] = max(dp[st][ed],  DFS(st, i) + DFS(i + 1, ed))

    return dp[st][ed]

DFS(0, n-1)
print(dp[0][n-1])
