import sys
input = sys.stdin.readline



n, m ,k = map(int, input().split())
ma = [int(input()) for _ in range(n)]
tree = [0] * 4 * n

def update(st, ed, idx, val, i):
    if st > idx or ed < idx:
        return 
    
    tree[i] += val
    if st != ed:
        mid = (st + ed) // 2
        update(st, mid, idx, val, i * 2)
        update(mid+1, ed, idx, val, i * 2 + 1)

for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(0, n-1, b, c, 1)


print(tree)