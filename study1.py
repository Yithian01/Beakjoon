import sys
input = sys.stdin.readline

le, ri = 0, 0 
n, m = map(int,input().split())

q = []
for _ in range(n):
    a = int(input())
    q.append(a)
    ri = max(ri, a+1)

# TTTTTTFFFFFFF  
# [           )  

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