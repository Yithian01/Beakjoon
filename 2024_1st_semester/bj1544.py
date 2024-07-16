# 시간복잡도 계산: N log N + N => O(N log N)
import sys
input = sys.stdin.readline
INF = 4 * (10 ** 6) 


n = int(input())
if n == 1 :
    print(0)
    exit(0)


q = []
vi = [True] * (n+1)
vi[0] = False
vi[1] = False
for i in range(2, n + 1):
    
    if vi[i]:
        q.append(i)

    j = 2

    while i * j <= n:
        vi[i * j] = False
        j += 1
    
ans, tmp = 0, 0
l, r = 0, 0
while True:
    if l == len(q):
        break
    
    if tmp < n and r < len(q):
        tmp += q[r] 
        r += 1
    
    else :
        tmp -= q[l]
        l += 1    

    if tmp == n:
        ans += 1

print(ans)