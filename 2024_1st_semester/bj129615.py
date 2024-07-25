from collections import deque
import sys
input = sys.stdin.readline

# (1) 모든 친구가 아닌 사람보다 앞에 있어야 한다.

n, m = map(int, input().split())
ma = list(map(int, input().split())) # 전체 배열
q = deque( list(map(int, input().split())) ) # 친구


ans = 0
st, ed = 0, n-1

while st < ed:
    a = ma[st]
    b = ma[ed]

    

    if a in q:
        st += 1
    
    elif b not in q:
        ed -=1

    else:
        ans += 1
        st += 1
        ed -=1



print(ans)