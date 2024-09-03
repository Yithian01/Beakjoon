# 하나의 열을 잡고 아래서 올라가면서 개수를 잡는다.
# c를 잡고 제일 아래 행이 1이면 기준점을 1올리고 시작


import sys
input = sys.stdin.readline


for _ in range(int(input())):
    n, m = map(int,input().split())
    ma = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    for c in range(m):
        
        bot = 0
        for r in range(n-1, -1, -1):
            
            if r == n-1:
                if ma[r][c] == 1:
                    bot = 1
                
                continue

            if ma[r][c] == 1:
                tmp = (n-1) - r 
                ans += tmp - bot
                bot +=1

    print(ans)
