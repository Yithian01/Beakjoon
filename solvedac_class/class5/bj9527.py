# 규칙1) 2^n -1 의 수까지 1의 개수 ==> 2^(n-1) + 2 * dp[n-1]
# 2^(n-1) => 이진수 변화시 앞자리에 붙는 1의 개수이다. 
#   ex) 0, 1, 10, 11, 100, 101, 110, 111, 1000 이라고 했을 때 
#       7까지의 1의 개수는 4, 5, 6, 7 즉 2^2 ~ 2^3-1까지의 제일 앞에 붙는 1의 개수 
#       그리고 나머지 3자리수는 이전까지의 2^2 -1 까지의  1의 값과 같다.

# 시간복잡도 계산: 최대 10^16까지 들어오고 log(10^16) => log(2^54) =>54회정도 
#                   O(2log(n))
import sys
input = sys.stdin.readline

dp = [0 for _ in range(60)]
for i in range(1, 60):
    dp[i] = 2 ** (i -1) + 2 * dp[i-1]

def sol(num):
    cnt = 0
    bn = bin(num)[2:] # 10을 넣으면 0b1010으로 변환해준다.
    bnLen = len(bn)
    
    for i in range( bnLen ):
        if bn[i] == '1':
            
            pow = bnLen-i-1
            cnt += dp[pow]  # 만약 10 이라면 (2^3-1 = 7)까지의 1의 개수와 2^3 ~ 10까지의 제일 앞의 1의 개수 구하면 된다.
            cnt += (num - 2 ** pow + 1) # 10이라면 8,9,10까지의 3개의 1을 더해주면 된다.
            num -= 2 ** pow # 제일 앞자리 삭제 
            
    return cnt

a, b = map(int, input().split())
print( sol(b) - sol(a-1) )