# 소인수는 항상 제곱근 이하에 있다.
# 최대 소인수는 항상 그 수의 제곱근 이하에 있다는 점입니다.
#예를 들어, n = 100이라고 가정하면
# 100의 제곱근은 10입니다. 따라서 100의 소인수는 10 이하에서 찾을 수 있다.
# 2와 5는 100의 소인수로, 10 이하에서 발견됩니다. 나머지 소인수는 이미 2와 5로 나누어 떨어진 나머지 값에서 파생됩니다.
# 소인수를 찾을 때 2부터 n의 제곱근까지 탐색하면 충분합니다. 왜냐하면 그 이후의 소인수는 이미 제곱근 이하의 소인수로 나누어 떨어지기 때문입니다.import sys
import sys
input = sys.stdin.readline


def sol(n):
    st = 2
    q = []
    while st * st < n + 1:
        if n % st == 0:
            q.append(st)
            n //= st
        
        else:
            st += 1

    if n > 1:
        q.append(n)

    return q


n, m = map(int, input().split())
if n == m :
    print(n)
    exit(0)

nq = [n]
mq = [m]
for i in sol(n):
    nq.append( n // i)
    n //= i

for j in sol(m):
    mq.append( m  // j)
    m //= j

print(max(list(set(nq)&set(mq))))
