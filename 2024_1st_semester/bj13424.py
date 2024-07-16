import sys
input = sys.stdin.readline
INF= 1e9


for _ in range(int(input())):
    n, m = map(int, input().split())


    ma = [[INF for _ in range(n+1)] for _ in range(n+1)]
    for _ in range(m):
        s, e, t = map(int, input().split())
        ma[s][e] = t
        ma[e][s] = t

    for i in range(1, n+1):
        ma[i][i] = 0

        
    for k in range(1, n+1): #경유지
        for i in range(1, n+1): #시작
            for j in range(1, n+1): # 도착지
                
                if ma[i][k] != INF and ma[k][j] != INF:
                    ma[i][j] = min(ma[i][j], ma[i][k] + ma[k][j])
                


    k = int(input())
    res = list(map(int, input().split()))
    ans = [0,INF] # 정답, 거리
    for i in range(1, n+1):
        
        tmp = 0
        for j in res:
            tmp += ma[j][i]

        if ans[1] > tmp:
            ans[0] = i
            ans[1] = tmp
    
    print(ans[0])
