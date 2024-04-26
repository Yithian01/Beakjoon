# (po + t) % n - 1 


# 1 2 3 4 5 6
# 0             => po = 0  n = 6,  t = 1    => ans = 0

# 2 3 4 5 6     => po = 0  n = 5 , t = 8    => ans = 2 
# 0 
#   0 
#     0 
#       0  
#          0
# 0
#   0 
#     0
import sys
input = sys.stdin.readline


n = int(input())
ma = [ (_ + 1) for _ in range(n)]    

le = len(ma)
t = 1
po = 0
for i in range(n-1):
    
    cnt = t ** 3
    po = (po + cnt) % le - 1
    if po < 0:
        po = le - 1

    ma.pop(po)
    t += 1
    le -=1


print(ma[0])