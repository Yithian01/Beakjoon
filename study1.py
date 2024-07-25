# 크루스칼, 프림, 다익스트라 사용하지 못하는 이유 
# 최소 신장 트리를 구하는 것이 아니다.
# n= 10^2 이라서 플로이드워샬사용 가능 -> O(N^3) -> 10^6 

# 예제1)
# 0 3 1 4 2 3  <-- 1
# 3 0 2 5 5 6  <-- 2
# 1 2 0 3 3 4  <-- 3
# 4 5 3 0 2 3  <-- 4
# 2 5 3 2 0 1  <-- 5
# 3 6 4 3 1 0  <-- 6
# 
# 3 5 

# 시간 복잡도: O(tN^3)
import sys
input = sys.stdin.readline
INF = 1e9

for _ in range(int(input())):
    n, m = map(int, input().split())
    ma = [[INF for _ in range(n+1)] for _ in range(n+1)]
    #ma = [[INF] * (n+1) for _ in range(n+1)]

    for _ in range(m):
        s, e, w = map(int, input().split())
        ma[s][e] = w
        ma[e][s] = w

    for i in range(1, n+1):
        ma[i][i] = 0
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                
                if ma[i][k] != INF and ma[k][j]:
                    ma[i][j] = min(ma[i][j], ma[i][k] + ma[k][j])
        
    k = int(input())
    minLen = INF
    ans = 0
    res = list(map(int,input().split()))
    for i in range(1, n+1):
        tmp = 0
        for j in res:
            tmp += ma[j][i] # 사람들이 있는 곳에서 i까지 걸리는 시간 --> sum(ma[j][i])
                            # ma[j] <-- 사람들이 있는 곳, ma[j][i] --> 어떤 사람이 j에 있는데 i까지 걸리는 시간
        
        if minLen > tmp:
            minLen = tmp
            ans = i
            

    print(ans)