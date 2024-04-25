# 크루스칼 알고리즘 
# 1) 시작, 도착, 가중치를 큐에 저장 --> q = []
# 2) 가중치를 기준으로 정렬 
# 3) nuion_find 를 통해서 연결된 가중치를 모두 더한다.
# 4) 연결된 횟수만큼 ( 1 * t ) + ( 2 * t ) ... ( n * t ) 를 추가로 더해준다.

# 시간복잡도 계산 : 정렬, union_find => n log n + n => O(n log n) 
import sys
input = sys.stdin.readline


def find(x):
    if ma[x] != x:
        ma[x] = find(ma[x])

    return ma[x]


n, m, t = map(int,input().split())
ma = [ _ for _ in range(n+1)]
q = []

cnt, ans = 0, 0


for i in range(m):
    s, e, w = map(int ,input().split())
    q.append((s,e,w))


q.sort(key=lambda x : x[2])

for s, e, w in q:
    s = find(s)
    e = find(e)

    if s != e:

        cnt += 1
        ans += w
        
        if s < e:
            ma[e] = s
        else:
            ma[s] = e
    

for i in range(1, cnt):
    ans += (i * t)

print(ans)