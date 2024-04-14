# 주소 : "https://www.acmicpc.net/problem/17828"

# 조건 : 26 * n => 최대 , n * 1 => 최소
# 문자열을 가장 작은 정렬값을 가지려면 앞의 index가 최소가 되어야 한다.
# AZAAA 보다 AAAZ가 더 작은 값을 보장 받는다.

# (1) 조건을 충족시키지 못한다면 "!"을 출력한다.
# (2) 1로 초기화된 n번 배열을 생성한다.
#     최소는 1이기에 [1] * n 이 된다.

# (3) 현재까지 최소 수는 AAA....(n개) 남은 분배 숫자는 m-n이다.
# (4) 이제 i ~ n개의 초콜릿을 ans가 0이 될때까지 최대 26개씩 순서대로 분배해준다.
# (5) 그러면 앞에 index부터 가장 많은 초콜릿 값을 가지게 된다.
# (6) 거꾸로 출력

# 시간 복잡도 계산 : 5 * 10^6 * 26 => 130 * 10^6 => 10^8정도
import sys
input = sys.stdin.readline
ma = {}

for i in range(26):
    tmp = 65 + i
    tmp = chr(tmp)
    ma[i+1] = tmp



n, m = map(int, input().split())
if 26 * n < m or m - n < 0 : 
    print('!')
    exit(0)


dp = [1] * n
ans = m - n

for i in range(n):
    if ans <= 0:
        break
    ans += 1
    tmp = 1
    while tmp < 26:
        tmp += 1
        if ans - tmp <= 0:
            break
    
    ans -= tmp
    dp[i] = tmp


for i in range(n-1, -1, -1):  
    print(ma[dp[i]],end='')