# INF에서 2를 뺴는 이유 
# 2018^2018 일 후 요일은? 현재 요일 월 
# 2018에서 7로 나눈다. ( 7주일이기 때문에 ) 나머지는 2 
# 2 % 2018 도 나머지가 2이다.
# 즉 2018 == 2( mod 7 )이 성립한다.
# 이제 양 항에 ^2018을 해주어도 나머지는 성립한다.
# 2018^2018 = 2^2018 (mod 7 )이다.
# 2^2018을 2^2  ( 2 ^ 2016) 이렇게 나눌 수 있다.
#   그리고 2^2016 은 (2^3)^672 으로 나타낼 수 있다.
#   그리고 mod 7을 취해주면 2^2 * (8 % 7)^672 로 나타낼 수 있다.
# 2^2 * (1)^672 => 4가 된다. 즉 2018^2018 => 4의 나머지가 된다.
# 현재 요일에서 4를 더해주면 금요일이 된다. 
# 
# 위 예제에서처럼 나머지가 1로 바뀌는 것의 승을 구하면 많은 양의 승을 생략할 수 있다.
import sys
input = sys.stdin.readline
INF = 10 ** 9 + 7
ans = 0

def multi(x, y):
    if y == 1: return x
    if y % 2 == 1 :
        return x * multi(x, y-1) % INF 
    
    t = multi( x, y // 2)
    return t * t % INF

def gcd(a,b):
    if b > a:
        a, b = b, a

    if b == 0 :
        return a
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

for _ in range(int(input())):
    n, m = map(int, input().split())
    
    k = gcd(n, m)  
    n //= k
    m //= k

    ans += m * multi(n, INF-2) % INF
    ans %= INF

print(ans)