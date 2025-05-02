import sys
input = sys.stdin.readline
INF = sys.maxsize
'''

최대 10^9이므로 : 99999999 -> 8자리
시간복잡도 계산 : 8c3 => O( nC3),    8 * 7 * 6 / 6 =>    56 * 6 => 336 / 6 = > 56정도
'''
ans = [INF, 0] # 최소, 최대
def sol(cnt, s):
    global ans

    for i in s:
        if int(i) % 2 != 0:
            cnt += 1


    if len(s) == 1:
        ans[0] = min(ans[0], cnt)
        ans[1] = max(ans[1], cnt)
        return 
    

    if len(s) == 2:
        a = int(s[0]) + int(s[1])
        sol(cnt, str(a))


    else:
        for i in range(1,len(s)-1):
            for j in range(i+1, len(s)):
                a = int(s[0:i]) + int(s[i:j]) + int(s[j:])
                sol( cnt, str(a))


n = input().rstrip()
sol(0, n)
print(*ans)