import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ma = list(map(int, input().split()))

if sum(ma) >= m:
    ans = 0

else:
    left = m
    feel, idx = 0, 0 # 시작 기분,  기분 인덱스
    
    while left > 0: # 방학이 남았다면 
        feel -= 1 
        if feel <= -1: # 오늘 기분 -1 ~ ??라면 
            if idx < n:
                feel = ma[idx]
                idx += 1
            
            else:
                break
        
        left -= 1
    
    cnt = left # 남은 일 수   
    ans = 0 # 정답
    idx = 1
    tmp = 1
    while idx <= cnt: #=> 남은 일수를 가장 균등하게 분배하기 ( 열린 공간으로 1이어도 들어갈 수 있게 )

        for i in range(n+1): # 균등하게 나오는 것은 3개면 4개가 가장 균등함 
            if idx > cnt: # 남은 일수보다 커지면 파괴
                break
            
            ans += (tmp ** 2)
            idx += 1
        tmp += 1


print(ans)