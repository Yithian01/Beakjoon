# 받으면서 st이 있거나 바로 전의 것이 b보다 크다면 즉 b가 작다면 st뺀다. ans += 1
import sys
input = sys.stdin.readline


ans = 0
q = []

for _ in range(int(input())):
    a, b = map(int, input().split())
    while len(q) > 0 and q[-1] > b: # 들어오는 수 b가 있는 수보다 작을 때 
        ans += 1
        q.pop()

    if len(q) > 0 and q[-1] == b:
        continue

    q.append(b)


while len(q) > 0:
    if q[-1] > 0:
        ans += 1
    q.pop()

print(ans)