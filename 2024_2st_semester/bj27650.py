import math
import sys
input = sys.stdin.readline



n = int(input())
INF= n + 1

q = []
vi = [False] * INF
for i in range(2, INF):
    if vi[i]:
        continue

    q.append(i)
    j = i * i
    while j < INF:
        vi[j] = True
        j += i

ans = 2
st, ed =  0, len(q) -1
# TTTFFFF
cnt = 0 
while st <= ed:
    if cnt == 20:
        break

    cnt += 1

    mid = (st + ed) // 2 
    tmp = q[mid]

    print(f'? {tmp}')
    sys.stdout.flush()
    m = int(input())
    
    if m == 0:
        ed = mid -1 
        ans = tmp
    else:
        st = mid + 1


print(f'! {ans}')
sys.stdout.flush()