import sys
input = sys.stdin.readline


def FIND(x):
    if x != num[x]:
        num[x] = FIND(num[x])
    return num[x]

def UNION(a, b):
    if b >= m:
        return 
        
    a = FIND(a)
    b = FIND(b)
    num[a] = b


n, m, k = map(int, input().split())
num = [ _ for _ in range(m)]
card = list(map(int, input().split()))
card.sort()  # 2 3 4 5 7 8 4 9

bruf = list(map(int, input().split()))
for i in bruf:
    # F F F F T T T T T 
    st, ed = -1 , len(card)-1 # [n-1, -1) 
    while st +1 < ed:
        mid = (st + ed ) // 2
        if card[mid] <= i:
            st = mid 

        else:
            ed = mid

    ans = FIND(ed)
    UNION(ans, ans+1)

    print(card[ans])
    
        