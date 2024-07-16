import sys
input = sys.stdin.readline


while True:
    try:
        a, b, c = map(float, input().split())
    except:
        exit(0)

    b /= 100
    # a돈을 b이자(%)임, c가 원하는 것 

    cnt = 0
    while a  < c :
        
        cnt += 1    
        tmp = a * b
        a += tmp

    
    print(cnt)