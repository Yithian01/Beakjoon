import sys
input = sys.stdin.readline

def convert(up):
    ss = ''
    for i in s:
        if ord(i) + up > 122: #123이 됬다면 들어감 
            ss += chr( ord(i) + up - 26)

        else:
            ss += chr( ord(i) + up )

    for i in q:
        if i in ss:
            return ss
    
    return -1

s = input().rstrip()
n = int(input())
q = []
for i in range(n):
    ss = input().rstrip()
    q.append(ss)

for i in range(26): # 알파벳은 26임 0 ~ 25까지 
    if convert(i) != -1:
        print(convert(i))
