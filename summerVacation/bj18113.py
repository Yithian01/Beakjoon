import sys
input = sys.stdin.readline

# 꼬다리 양쪽 균일하게 제거   n > 2k 
# 꼬다리 한쪽만 제거  n <= 2k  
# 길이가 같으면 폐기 n <= k

maxKim = -1

n, k, m = map(int, input().split())
ma = []
for _ in range(n):
    i = int(input())    
    tmp = 0
    if i >= (2 * k):
        if i > (2 * k):
            tmp = i - (2 * k)
            ma.append(tmp)

    elif i > k:
        tmp = i - k
        ma.append(tmp)


    maxKim = max(maxKim, tmp)

ans = -1
st, ed = 1, maxKim

while st <= ed:
    mid = (st + ed) // 2
    p = 0 

    for i in ma:
        p += (i // mid) # 조각 나누기   
    
    if m <= p:
        ans = mid
        st = mid + 1
    
    else:
        ed = mid -1

print(ans)


