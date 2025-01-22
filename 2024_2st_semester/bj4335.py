import sys
input = sys.stdin.readline

ans = [1, 10]  # 정답가능 위치 
# [1, 9]     [4, 9]   $ 틀린 경우 2는 너무 높다  
# 즉 최하보다 작을 경우
#    최대보다 클 경우
isLie = False
while True:
    n = int(input())
    
    if n == 0:
        break

    s = input().rstrip()
    
    if s == 'right on':
        if isLie:
            print('Stan is dishonest')
        else:
            if ans[0] <= n <= ans[1]:
                print('Stan may be honest')
            else:
                print('Stan is dishonest')


        ans = [1, 10] # 초기화 
        isLie = False
        continue

    # [1, 8]


    if s == 'too high':   
        if ans[0] > n:
            isLie = True
        
        else:
            if ans[1] >= n:
                ans[1] = n-1
    else:
        if ans[1] < n:
            isLie = True

        else:
            if ans[0] <= n:
                ans[0] = n + 1

