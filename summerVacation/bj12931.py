#주어진 ma의 sum()이 0이 될 떄 까지 역행
#1) ma를 모두 훓으면서 홀수면 -1해주기 이 때 cnt += 1 
#2) (1)에서 sum(ma)가 0인지 체크 0이면 할 필요 없음 
#3) 남은 수 ma가 짝수 or 0인 것이 확정이므로 각 칸 /2해주고 (3)과정이 cnt + 1 해주기 

#시간복잡도 계산 : log(N) 만큼 n을 반복 하므로  O(Nlog(N))
import sys
sys.stdin.readline

n = int(input())
ma = list(map(int, input().split()))

cnt = 0
while sum(ma) > 0:
    
    for i in range(n):
        if ma[i] % 2 != 0:
            cnt += 1
            ma[i] -= 1
    
    if sum(ma) == 0:
        break

    cnt += 1
    for i in range(n):
        ma[i] /= 2
    

print(cnt)

    