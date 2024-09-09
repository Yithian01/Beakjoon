# 제일 위의 행 0을 잡고 m-1까지 본 뒤 제일 뒤의 1을 잡는다.
# 현재 행의 1인 곳까지 0으로 만들어 준다.
# 다음행은 이전에 잡은 열부터 본다 이미 끝 행이라면 그 순간부터는 아래로만 보게 된다.

# 즉 "ㄱ"자로 보게되는 것이다.
# 최대 계단식으로 보게 된다 1번의 시도에 

#시간 복잡도 계산: NM을 여러번 보게 될 경우가 있다 이경우 아래의 코드로는 O( (NM)^2 )이 나올것이다.


n, m = map(int, input().split())
ma = [list(map(int, input().split()))for _ in range(n)]


def sol():
    last = 0
    for i in range(n):
        ed = last 
        for j in range(last, m):
            if ma[i][j]:
                ed = j  # 현재 j를 기준으로 잡기 
            
        
        for j in range(last, ed+ 1):
            ma[i][j] = 0 # 현재까지 i는 고정임, j만 옮기면 0으로 변경

        last =  ed# 시작하는 행을 ed로 변경 


ans = 0 
while sum(map(sum, ma)):
    sol()
    ans += 1
print(ans)