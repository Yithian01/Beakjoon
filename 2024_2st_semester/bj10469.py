from collections import deque
import sys
input = sys.stdin.readline

q = deque()
ma = [ list(input().rstrip()) for _ in range(8)]
for i in range(8):
    for j in range(8):
        if ma[i][j] == '*':
            q.append((i,j))


if len(q) != 8:
    print("invalid")
    exit(0)



def rowCheck(r, c):
    for i in range(8):
        if i != r and ma[i][c] == '*':
            return False
    
    return True

def colCheck(r, c):
    for j in range(8):
        if j != c and ma[r][j] == '*':
            return False
    
    return True

def crossCheck(r, c):
    for i in range(1, 8):
        nr = r + i 
        nc = c + i
        if nr < 0 or nr >= 8 or nc < 0 or nc >= 8:
            continue
        
        if ma[nr][nc] == '*':
            return False
        
    for i in range(1, 8):
        nr = r - i 
        nc = c - i
        if nr < 0 or nr >= 8 or nc < 0 or nc >= 8:
            continue
        
        if ma[nr][nc] == '*':
            return False

    for i in range(1, 8):
        nr = r + i 
        nc = c - i
        if nr < 0 or nr >= 8 or nc < 0 or nc >= 8:
            continue
        
        if ma[nr][nc] == '*':
            return False

    for i in range(1, 8):
        nr = r - i 
        nc = c + i
        if nr < 0 or nr >= 8 or nc < 0 or nc >= 8:
            continue
        
        if ma[nr][nc] == '*':
            return False
                
    return True
    


for cr, cc in q:
    if (not rowCheck(cr, cc)) or (not colCheck(cr, cc)) or ( not crossCheck(cr, cc)):
        print("invalid")
        break

else:
    print("valid")