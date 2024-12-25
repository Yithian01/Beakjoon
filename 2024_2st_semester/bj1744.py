import sys
input = sys.stdin.readline


n = int(input())
up = []
down = []
cnt = 0 

for _ in range(n):
    m = int(input())
    if m == 0:
        cnt += 1
    
    elif m < 0:
        down.append(m)
    else:
        up.append(m)

up.sort()
down.sort(reverse=True)

ans = 0
isUp = False
for i in range(len(up) -1, -1, -1):
    if isUp:
        isUp = False
        continue

    if i > 0 and up[i] <  up[i] * up[i-1] :
        ans += up[i] * up[i-1]
        isUp = True

    else:
        ans += up[i]


# 음수 처리 두개씩 가능하다면 처리 
for i in range(len(down)-1, 0, -2):
    ans += down[i] * down[i-1]


if len(down) % 2 == 1:
    if cnt > 0:
        ans += 0 # 0이랑 초기화
    else:
        ans += down[0]

print(ans)