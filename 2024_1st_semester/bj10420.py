import sys
input = sys.stdin.readline

def isYear(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)


def isMonth(y, m):
    if m in [4,6,9,11]:
        return 30
    
    elif m == 2:
        return 29 if isYear(y) else 28
    else:
        return 31


def sol(y, m, day, days):
    while days > 0:
        tmp = isMonth(y, m)    # 현재 30일을 넘어가면 안된다. 4월 이므로 
        if day + days <= tmp:  # 더한 날이 해당날을 넘어가지 않으면
            day += days        # 그대로 하고 추가되는 날은 있지 않다.
            days = 0
        
        else:
            days -= (tmp - day + 1) # 30 - 2 + 1 = 28일을 사용해서 30일을 채우고            day = 1                 #
            day = 1                 # 1일을 추가해 다음달 1일로 이동
            m += 1                  
            if m > 12:              # 월이 넘어가면 년을 1일 올려준다.
                m = 1
                y += 1

    res = str(y) + '-' 
    if m // 10 == 0:
        res += '0' 
    res += str(m) + '-'

    if day // 10 == 0:
        res += '0' 
    res += str(day)

    return res


st = [2014, 4, 1]
n = int(input())

print( sol(st[0], st[1], st[2], n) )