# 만약 3개가 아닌 3개 이상으로 달라진다면? 추가 재귀 필요
 
#시간복잡도 계산 : 9c3 => O( nC3),    9 * 8 * 7 / 6 =>    56 * 9 => 494 / 6 = > 83정도
#  ㄴ> 그런데 이후 9C3 은 ->  7C3으로 변경된다. -> 5C3 -> 3C3  으로  1c3이 될 때까지 호출되므로 일반화 불가능하다.
import sys
input = sys.stdin.readline
INF = 1e9

ans = [INF, -INF] # min, max

def bt(s, tmp):
    res = tmp

    for i in s:
        if int(i) % 2 != 0:
            res += 1    # 현재까지 오면서의 홀수값

    if len(s) == 1:
        ans[0] = min(ans[0], res)   # 홀수 최소값 
        ans[1] = max(ans[1], res)   # 홀수 최대값
        return 
    
    if len(s) == 2:
        bt(str( int(s[0]) + int(s[1]) ), res)

    else:
        for i in range(1, len(s) -1):
            for j in range(i+1, len(s)):
                bt( str( int(s[0:i]) + int(s[i:j]) + int(s[j:]) ), res)



n = input().rstrip()
bt(n, 0)

print(*ans)