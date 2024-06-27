import sys
input = sys.stdin.readline

# 자주 나오면 앞에 
# 길이가 길면 앞에 
# 사전 순 앞에
table = {}
n, m = map(int, input().split())
for _ in range(n):
    s = input().rstrip()
    if len(s) < m:
        continue

    if s not in table:
        table[s] = 0 

    table[s] += 1

ma = sorted(table.items(), key= lambda x : (-x[1], -len(x[0]), x[0]))
for i in ma:
    print(i[0])