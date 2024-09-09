from heapq import heappush, heappop
import sys
input = sys.stdin.readline
INF = 1e9

# 내구도, 무게 
#   7      5
#   3      4
#   치는 쪽면 서로 감소 대각선으로 

n = int(input())

ma = []
na = [0] * (n)
vi = [1] * (n)
for i in range(n):
    a, b = map(int, input().split())
    ma.append((a, b, i))
    na[i] = a

ans = 0
pos = 0
for i in range(n):
    if sum(vi) <= 1:
        break

    cw = ma[pos][1] # 현재 무게
    tmp = sorted(ma, key=lambda x: (x[1],x[0]))
    print(f'tmp = {tmp}')
    
    nn = -1
    for j in range(n):
        if tmp[j][2] == 0 or vi[tmp[j][2]] == 0:
            continue
        
        else:
           nn = j
           break


    na[pos] -= tmp[j][1]
    na[tmp[j][2]] -= cw
    if na[pos] <= 0:
        ans += 1
        vi[pos] = 0

    if na[tmp[j][2]] <= 0:
        ans += 1
        vi[tmp[j][2]] = 0


    while True:
        pos += 1
        if pos == n-1 or vi[pos] == 1 :
            break

    if pos == n-1:
        break


print(ans)