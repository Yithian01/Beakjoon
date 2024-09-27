# 두 개씩의 쌍을 구한다.
# 그리고 i, j 의 idx를 더했을 때 0이라면 만약 

# 시간복잡도 계산: N^2 * log N
#    N = 4 * 10^3 :   10^7 * 10 => 10^8 보다 조금 작은 수 
import sys
input = sys.stdin.readline

n = int(input())
ma =[list(map(int, input().split()))for _ in range(n)]

ab, cd = [], []
for i in range(n):
    for j in range(n):
        ab.append(ma[i][0] + ma[j][1])
        cd.append(ma[i][2] + ma[j][3])

ab.sort()
cd.sort()

ans = 0
st , ed = 0, len(cd) -1
while st < len(ab) and ed >= 0: 
    if ab[st] + cd[ed] == 0:
        nst, ned = st + 1, ed - 1
        while nst < len(ab) and ab[nst] == ab[st]:
            nst += 1
        while ned >= 0 and cd[ned] == cd[ed]:
            ned -= 1

        ans += (nst - st) * (ed - ned)
        st, ed = nst, ned  
    
    elif ab[st] + cd[ed] > 0:
        ed -=1
    else:
        st += 1

print(ans)