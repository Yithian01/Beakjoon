#5C3이므로 5 4 3 => 60 / 6 => 10가지 경우의 수 
import sys
input = sys.stdin.readline

ans = 1
res = 0

n = int(input())
for t in range(n):
    cnt = t + 1

    ma = list(map(int, input().split()))
    
    for i in range(3):
        for j in range(i+1, 4):
            for k in range(j+1, 5):
                tmp = (ma[i] + ma[j] + ma[k]) % 10
                if res <= tmp:
                    res = tmp 
                    ans = cnt
                    
                

print(ans)