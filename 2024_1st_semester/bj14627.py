# 반례 
# 3 5
# 100
# 100
# 100
# 필요한 개수와 최대 길이를 곱한 것을 빼주어야 한다. 나머지 연산은 불가능!!!

# 시간 복잡도 계산: O( s * logN ) -> 10^6 * log 10^9 
#      log 10^9 => 2^30 => 30 -> 3 * 10 * 10^6 => 3 *10^7정도 
import sys
input = sys.stdin.readline

le, ri = 0, 0
# 사온 파, 주문 개수
n, m = map(int, input().split())
q = []
for _ in range(n):
    a = int(input())
    q.append(a)
    ri = max(ri, a+1)

# TTTTTTFFFFF   [ )
# le = 0
# ri = max(q)
while le + 1 < ri:
    mid = (le + ri) // 2

    tmp = 0
    for i in q:
        tmp += i // mid
    
    if tmp >= m:
        le = mid
    else:
        ri = mid

ans = 0
ans += sum(q) - (le * m)
print(ans)