# 같아져야 한다.

# 시간복잡도 게산: 100 * 1000 => 10^5 정도 
# s = 1, t = 100일때 최대 10^3번 반복함

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    s, t = map(int, input().split())
    # 2가지 방법 
    # s * 2 , t + 3
    # s + 1
    q = deque()
    q.append((s,t, 0))
    
    while q:
        cs, ct, cw = q.popleft()
        
        if cs == ct:
            print(cw)
            break
        elif cs > ct:
            continue
        
        q.append((cs + 1, ct , cw + 1))
        q.append((cs + cs, ct + 3 , cw + 1))

    
