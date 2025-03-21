import sys
#  0 st---->           1 <----st

n, m = map(int, sys.stdin.readline().split())
ma = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if b == 0:
        ma.append(  [b, [0, a]] )
    else:
        ma.append(  [b, [m-a, m]] )

cnt, st = 0, 0
while True:
    cst, ced = ma[st][1]
    tmp = st
    for i in range(tmp + 1, n):
        nst, ned = ma[i][1]

        if ced < nst or cst > ned:
            break

        else:
            cst, ced = nst, ned
            st += 1

    if st == n-1:
        break


    for i in range(st, n):
        
        if ma[i][0] == 0:  # 물체가 0 방향으로 가고 있으면
            ma[i][1][0] += 1
            ma[i][1][1] += 1
            if ma[i][1][1] == m:  # 끝에 도달하면 방향을 반대로
                ma[i][0] = 1

        elif ma[i][0] == 1:  # 물체가 1 방향으로 가고 있으면
            ma[i][1][0] -= 1
            ma[i][1][1] -= 1
            if ma[i][1][0] == 0:  # 처음에 도달하면 방향을 반대로
                ma[i][0] = 0
        
    
    cnt += 1

print(cnt)