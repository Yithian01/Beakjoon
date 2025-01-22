import sys

while True:
    n = int(input())

    if n == 0:
        break


    ma = [ 0 for _ in  range(n+1)]
    tmp = list(input().rstrip().split(','))

    for i in tmp:
        
        if '-' in i:
            a, b = map(int, i.split('-'))
            
            for j in range(a, b + 1):
                if j <= n:
                    ma[j] += 1

            
            continue

        k = int(i)

        if k <= n:
            ma[k] += 1
    
    ans = 0 
    for i in ma:
        if i >= 1:
            ans += 1

    print(ans)