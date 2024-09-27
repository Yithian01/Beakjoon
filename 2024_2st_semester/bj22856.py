import sys
sys.setrecursionlimit(10** 8)
input = sys.stdin.readline

n = int(input())
ma =[[] for _ in range(n+1)]
for _ in range(n):
    i, le, ri = map(int, input().split())
    ma[i].append(le)
    ma[i].append(ri)

vi = [0] * (n+1)
ans = []
def bt(k):
    global ans
    ans.append(k)
    vi[k] = 1
    
    if ma[k][0] != -1:
        bt(ma[k][0])
        ans.append(k)

    
    if ma[k][1] != -1:
        bt(ma[k][1])
        ans.append(k)

tmp = 0
def check(k):
    global tmp
    if ma[k][1] == -1:
        return 
    
    else:
        tmp += 1
        check(ma[k][1])


bt(1)
check(1)
print( len(ans) -tmp - 1)
