import sys
input = sys.stdin.readline
INF = 10^6 + 1
# N = 10^5 이므로 N^2은 불가 다른 방법 필요
# 3 4 12 일때 

# 3 : 4 =  0 : 0
# 3 : 12 = 1 : -1
# 4 : 12 = 1 : -2


# 최대 숫자의 수가 10^6이고 한번만 등장 
# 자기 자신으로 나눠 지는 큰수 10^6보다 작은 수에 -1을 해주고 자신을 1해주면 

n = int(input())
ma = list(map(int, input().split()))

tmp = ma.copy()
ma.sort() # N log N => 10^7 이하 
res = max(ma)

ta = {}
for i in ma: # N 
    ta[i] = 0

for i in ma: # N

    cnt = 2
    while (i * cnt) <= res:  #  LOG 2 <--- 최악의 경우 2인 경우임
        if (i * cnt) in ta:
            ta[(i * cnt)] -= 1
            ta[i] += 1

        cnt += 1

for i in tmp:
    print(ta[i], end=' ')
