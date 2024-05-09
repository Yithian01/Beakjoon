# 자기자신의 index값을 넘겨주어서 호출한다.
# 자기보다 작은 값을 출력하지 않음 
import sys
input = sys.stdin.readline

q = []
def bt(cnt):
    if len(q) == m:
        print(*q)
        return 
    
    else:
        for i in range(cnt, n):
            q.append(ma[i])
            bt(i)
            q.pop()

    return

n, m = map(int, input().split())
ma = list(map(int, input().split()))
ma.sort()
bt(0)
