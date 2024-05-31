import sys


n, k = map(int, input().split())
ma = [[] for _ in range(n+1)]

while True:
    a, b = input().rstrip().split()
    a = int(a)
    if a == 0:
        break

    if len(ma[a]) == k:
        continue    

        
    ma[a].append(b)


for i in range(1, n+1, 2):
    ma[i].sort(key = lambda x : (len(x), x))
    for j in ma[i]:
        print(i, j)
    
    
for i in range(2, n+1, 2):
    ma[i].sort(key = lambda x : (len(x), x))
    for j in ma[i]:
        print(i, j)