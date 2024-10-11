import sys
input = sys.stdin.readline


def sol(a, b):
    
    while True:
        
        if a > b: # a가 무조건 작게
            a, b = b, a

        if a == 1:
            return 1

        if b % a == 0:
            return a
    
    else:
        
    

while True:
    try:
        n, m = map(int, input().split())
    except:
        break

    ans = -1
