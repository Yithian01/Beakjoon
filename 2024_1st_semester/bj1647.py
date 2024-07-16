import sys
input = sys.stdin.readline

def FIND(x):
    if ma[x] !=x:
        return FIND(ma[x])

    return ma[x]


n, m = map(int, input().split())

MAXLEN = 0
q = []
ma = [ _ for _ in range(n+1)]

for _ in range(m):
    s, e, t = map(int, input().split())
    q.append((t, s, e))
    MAXLEN += t


ans = 0
q.sort(key=lambda x : x[0])
vi =[]

for w, cs, ce in q:


    s = FIND(cs)
    e = FIND(ce)

    if s > e:
        s, e = e, s
    
    if s != e:
        vi.append(w)
        ans += w

    ma[e] = s # 큰거를 작은 거에 할당 


print(sum(vi) - max(vi))

