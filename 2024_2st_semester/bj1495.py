import sys
input = sys.stdin.readline

''' 
    뿌리로 계속 뻗어나가면 가능한 경우의 수는 2^N임 푸르닝으로 줄일수 있는가?
    2^10 => 10^3 정도이므로 2^50 => 10^15 고로 2^N은 불가능
    그렇다고 M에 가까운 것을 항상 최선으로 유지는 불가능 
    DAG 가능??  앞의 것만 영향을 받음 하지만 어디가 최선인지 모른다.

    해결방법 : 단순한 그리디DP 수가 더 커지면 불가능 but 50*10^3 => 5*10^4이므로 가능
    
    
    

'''
n, s, m = map(int, input().split())
ma = list(map(int, input().split()))
dp = [[False] * (m+1) for _ in range(n)]
if s - ma[0] >= 0:
    dp[0][s- ma[0]] = True
if s + ma[0] <= m:
    dp[0][s + ma[0]] = True


ans = -1
for i in range(1, n):
    for j in range(m+1):
        if dp[i-1][j]:
            if j - ma[i] >= 0:
                dp[i][ j - ma[i] ] = True
            
            if j + ma[i] <= m:
                dp[i][ j + ma[i] ] = True


ans = -1
for j in range(m + 1):
    if dp[n-1][j]:
        ans = j

print(ans)