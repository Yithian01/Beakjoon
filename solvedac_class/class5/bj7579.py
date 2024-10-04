# 배낭 문제 
# r = 종류, c = 코스트
# 현재 메모리 크기 = cw, 코스트 = cc 라고 할 때 
# 메모리 크기를 1 ~ 최대갑 INF( 10^7)까지 돌린다. 
# 현재 메모리 크기에 도달하면 [i-1][j - cw]만큼을 제외한 인덱스의 값( 메모리 크기)를 변경

# 의문: 공간 복잡도가 터지지 않을까?
# 128MB => 128 * 10^6 --> int형 매트릭스 --> 10^8 정도인데 열만 10^8이다.
# but 여기서는 100 정도밖에 안되는 cost를 잡으므로 터지지 않는다.

# 아 왜 이 간단한 걸 그냥 cost를 0부터 시작하면 되는데

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))
ans = sum(b) 

dp = [[0 for _ in range(ans+1)] for _ in range(n+1)]

for i in range(1, n+1):
    cw = a[i]
    cc = b[i]

    for j in range(ans+1):
        if j < cc:                # 현재 바이트가 작다면 
            dp[i][j] = dp[i-1][j] # 이전값을 물려받는다.
        
        else:
            dp[i][j] = max(dp[i-1][j-cc] + cw, dp[i-1][j])
            
        if dp[i][j] >= m:
            ans = min(ans , j) 


if m != 0:
    print(ans)
else:
    print(0)