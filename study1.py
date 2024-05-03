import sys
input = sys.stdin.readline

n, m = map(int, input().split())
w = input().rstrip()
s = input().rstrip()

wa = [0] * 60 
sa = [0] * 60 


ans = 0
st, ed = 0, 0

for i in w:
    wa[ord(i) - 65] += 1


for i in range(len(s)):
    sa[ord(s[i]) - 65] += 1
    ed += 1

    if ed == n:
        
        if wa == sa:
            ans += 1
        
        sa[ord(s[st])- 65] -= 1
        st +=1
        ed -= 1

print(ans)