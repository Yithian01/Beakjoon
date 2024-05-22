# 최대 100개의 개수의 100줄의 문제 
# 정답 배열의 최소 길이 3자 

# 시간복잡도 계산 : 10000 // 3 => 3 * 10^3승 정도 10^4 * 10^3 => 10^7보다 작을 것이다.  
import sys
input = sys.stdin.readline


def check(s):
    sLen = len(s)
    for st in range(sLen):
        if s[st] == ss[0]:
            for ed in range(st, sLen):
                if s[ed] == ss[-1]:

                    tmp = (ed - st) // (len(ss) - 1) # 현재 문자열 길이
                    cnt = 1
                    while cnt < len(ss):
                        if s[st + (cnt * tmp)] == ss[cnt]:
                            cnt += 1
                            continue
                        
                        break
                    else:
                        return 1
    
    return 0
                    

n = int(input())
ss = input().rstrip()
q = list(input().rstrip() for _ in range(n))

ans = 0
for i in q:
    ans += check(i)

print(ans)