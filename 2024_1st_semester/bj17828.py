# 26 * n => 최대 
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

if m > (26 * n) and m < (1 * n): 
    print('!')
    exit(0)

ans = m - n
q = [1] * n
for i in range(n):
    tmp = q[i]
    for j in range(25):
        if ans - tmp + 1 < 0: break
        tmp += 1
        
    if tmp != 1:
        ans -= tmp
    if ans == 0:
        break

    q[i] = tmp


res = 0
for i in range(len(q)):
    res += q[i]

print(f'res = {res}')
