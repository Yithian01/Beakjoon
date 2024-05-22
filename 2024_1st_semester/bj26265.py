import sys
input = sys.stdin.readline

ma = {}
s = []
for _ in range(int(input())):
    a, b = map(str, input().rstrip().split())
    if a not in ma:
        ma[a] = []
    
    ma[a].append(b)
    s.append(a)

s = sorted(set(s))
for i in s:
    li = sorted(ma[i], reverse=True)
    for j in li:
        print(i, j,sep=' ')
    