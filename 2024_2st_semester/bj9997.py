import sys
input = sys.stdin.readline
# 비트 마스킹 조합을 찾으면 터진다. 문자열이 최대 10^2 이므로 
# O(2^n * n * 26) <---- 2^26 * 26 * 26 => 10^7 * 2 * 10^2 => 2 * 10^9 정도 터진다.
# 비트 마스킹 사용 : 2^26 * 26 => 10^8 정도


def BT(idx, res):
    global ans, n 
    

    if idx == n:
        
        if num == res:
            ans += 1

        return 
    
    BT(idx + 1, res | ma[idx])
    BT(idx + 1, res )


n = int(input())
ma = [0] * n 

for i in range(n):
    s = input().rstrip()
    
    for j in s:
        ma[i] |= (1 << ord(j) - 97)

    
num = (1 << 26) - 1
ans = 0

BT(0, 0)

print(ans )