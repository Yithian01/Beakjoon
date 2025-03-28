import sys
input = sys.stdin.readline

'''
    문제의 최대 n = 10^6 => 2^20
    트리의 크기 = 1 << 21로 설정하면 터지지 않음 

    bois를 20으로 주고 설정 <-- 이렇게 해야 최대 크기 트리끝까지 갈 수 있음
    bois + a >> 1 계속 해주면 홀, 짝을 알아서 처리해서 트리에 들어감 

'''
tree = [0] * (1 << 21)
bios = 1 << 20

def sol(st, ed):
    st += bios
    ed += bios

    ans = 0
    while (st <= ed):
        if (st % 2 == 1):
            ans += tree[st]
            st += 1
        
        if(ed % 2 == 0):
            ans += tree[ed]
            ed -= 1

        st >>= 1
        ed >>= 1
    return ans



n, m =map(int, input().split())
for _ in range(m):
    
    a, b, c = map(int, input().split())
    if a == 1:
        b += bios
        while(b):
            tree[b] += c
            b >>= 1
    
    else:
        print(sol(b, c))
