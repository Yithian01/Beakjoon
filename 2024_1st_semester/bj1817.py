# 시간복잡도 계산 : 10^6 LOG  10^6  => 10^6 * 2^20 => 2* 10^7 정도
import sys
input = sys.stdin.readline
INF = (10**6) + 1

for _ in range(int(input())):
    n = int(input())
    
    for i in range(2, INF):
        if n % i == 0:
            print("NO")
            break
        
    else:
        print('YES')