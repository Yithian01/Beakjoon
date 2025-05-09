import sys
input = sys.stdin.readline
''''
    투포인트: a, c를 정하고 b를 통해 구한다. -> O(N^2) 정도 

    양끝점을 잡아두고 그 수에 2로 나누어 떨어지는 수가 있는지 확인 있다면 +1 



'''

for _ in range(int(input())):
    ans = 0
    n = int(input())
    ma = list(map(int, input().split()))

    ma.sort()

    se = set(ma)

    for i in range(n):
        for j in range(i+1, n):
            a = ma[i]
            c = ma[j]
            if (a + c) % 2 == 0:
                b = (a + c) // 2

                if b in se:
                    ans += 1

    print(ans)         