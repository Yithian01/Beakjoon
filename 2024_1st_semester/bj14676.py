# 위상 정렬 => 해당 노드를 가기 전에 해야 될 이전 노드
import sys
input = sys.stdin.readline
   
n, m, k = map(int, input().split())
ma = [[] for _ in range(n+1)]
num = [0] * (n+1)

for _ in range(m):
    s, e = map(int, input().split())
    ma[e].append(s)



isCheck = False
for _ in range(k):

    s, e = map(int, input().split())

    if s == 1:
        for i in ma[e]:
            if num[i] < 1:
                isCheck = True
                break
        
        if not isCheck:
            num[e] += 1

    elif s == 2:
        if num[e] < 1:
            isCheck = True
        
        else:
            num[e] -= 1
            
if not isCheck:
    print("King-God-Emperor")
else:
    print("Lier!")