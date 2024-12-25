import sys
input = sys.stdin.readline

s =input().rstrip()
a_cnt = 0 

for i in s:
    if i == 'a':
        a_cnt += 1

ans = []
for i in range(len(s)):
    cnt = 0
    
    for j in range(a_cnt):
        idx = (i + j) % (len(s))
        
        if s[idx] == 'b':
            cnt += 1
    
    ans.append(cnt)

    
print(min(ans))