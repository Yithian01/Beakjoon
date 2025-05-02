from itertools import permutations as per
import sys
input = sys.stdin.readline
INF = sys.maxsize
'''
    [0, 1, 2, 3, 4, 5, 6, 7, 8]
    매직 스퀘어 공식 
        012 == 345 == 678
        048 == 246 
        036 == 147 == 258
    
'''
ma = []
for _ in range(3):
    for i in map(int, input().split()):
        ma.append(i)
ans = INF


for i in per([_ + 1 for _ in range(9)]):
    if i[4] != 5:
        continue

    a = sum(i[0:3])
    b = sum(i[3:6])
    c = sum(i[6:9])

    d = i[0] + i[4] + i[8]
    e = i[2] + i[4] + i[6] 

    f = i[0] + i[3] + i[6]
    g = i[1] + i[4] + i[7]
    h = i[2] + i[5] + i[8]

    q = set()
    q.add(a)
    q.add(b)
    q.add(c)
    q.add(d)
    q.add(e)
    q.add(f)
    q.add(g)
    q.add(h)

    if len(q) == 1:

        tmp = 0
        for idx in range(9):
            tmp += abs(ma[idx] - i[idx])
        
        ans = min(ans, tmp)
print(ans)
