import sys
input = sys.stdin.readline


n = int(input())
ma =list(int(input()) for _ in range(n))


def sol(a, b, cnt, st, ed):
    if cnt == n:
        return 
    
    # 상대면 규칙이있음 
    if cnt % 2 == 0:
        if ma[st] > ma[ed]:
            st = (st -1 + n) % n
            sol(a, b + ma[st], cnt + 1, st , ed)
        else:
            ed = (ed + 1 + n) % n
            sol(a, b + ma[ed], cnt + 1, st , ed)
            
    else:
        st = (st -1 + n) % n
        sol(a, b + ma[st], cnt + 1, st , ed)
        st = (st +1 +n ) % n
        ed = (ed + 1 + n) % n
        sol(a, b + ma[ed], cnt + 1, st , ed)
        ed = (ed - 1 + n) % n
    # 나는 랜덤



ans = 0
for i in range(n):
    # 나는 아무거나 선택 
    st = (i -1 +n )% n
    ed = (i +1 +n)% n
    ans = max(ans, sol(ma[i], 0, 0, st, ed) )

print(ans)
    