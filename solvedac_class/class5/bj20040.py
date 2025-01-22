import sys
input = sys.stdin.readline
sys.setrecursionlimit(5 * 10 ** 5 +1)

n, m = map(int, input().split())
node = [_ for _ in range(n)]

def FIND(x):
    
    if node[x] != x:
        node[x] = FIND(node[x])

    return node[x]

isAns = False
ans = 0
cnt = 0
for _ in range(m):
    cnt += 1
    a, b = map(int, input().split())
    if isAns:
        continue
    
    st = FIND(a)
    ed = FIND(b)
    
    if st == ed:
        ans = cnt
        isAns = True
        continue

    if st > ed:
        st, ed = ed , st

    node[st] = ed 

if isAns:
    print(ans)
else:
    print(ans)