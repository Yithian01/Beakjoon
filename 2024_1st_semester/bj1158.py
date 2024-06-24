import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ma = [ _ + 1 for _ in range(n)] # 8
q = []

be = m - 1
while ma:
    l = len(ma)
    be %= l
    q.append(ma.pop(be))
    be += (m - 1)

print('<', end='')
for i in range(n):
    if i == n-1:
        print(q[i], end='>')
    else:
        print(q[i], end=', ')
