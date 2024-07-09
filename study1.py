# 이긴팀 점수 올리기 

# 동점이면 
#   이전에 1이 이겼으면 ans[1] += time - 이전 시간 
#   이전에 2가 이겼으면 ans[2] += tine - 이전 시간 
#   이전 값 비김 (0= 비김, 1, 2)

# 1이 이겼으면 
#   이전 값 비김, 이기기 시작한 값을 넣고, 1이 이겼다고 표시 

# 2가 이겼으면 
#   이전 값 비김, 이기기 시작한 값을 넣고 2가 이겼다고 표시 

# 이긴 사람이 에게 48분 뺸 값 넣어주기 
import sys
input = sys.stdin.readline

# [이기기 시작한 값, 전에 이긴 사람]   0이면 비김, 1, 2 
last = [0] * 2
goal = [0] * 3
ans = [0] * 3 

for _ in range(int(input())):
    a, b = map(str, input().split())
    a = int(a)
    mi, se = map(int, b.split(':'))
    time = mi * 60 + se
    goal[a] += 1

    if goal[1] == goal[2]:
        if last[1] == 1:
            ans[1] += time - last[0]
        elif last[1] == 2:
            ans[2] += time - last[0]
        last[1] = 0

    else:
        if last[1] == 0:
            last[0] = time
            last[1] = a 
        

ans[ last[1] ] += (60 * 48) - last[0]
for i in range(1, 3):
    me, se = ans[i] // 60, ans[i] % 60
    s = ''
    if me // 10 == 0:
        s += '0' + str(me) + ':'
    else:
        s += str(me) + ':'

    if se // 10 == 0 :
        s += '0' + str(se)
    else:
        s += str(se) 

    print(s)