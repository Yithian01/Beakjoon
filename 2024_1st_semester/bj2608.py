import sys
input = sys.stdin.readline

ta = {"I" : 1 , "V" : 5, "X" : 10
      ,"L" : 50 ,  "C" : 100, "D" : 500, "M": 1000}

ma = {"IV" : 4, "IX" : 9, "XL" : 40, "XC" : 90, "CD": 400, "CM" : 900}
s1 = input().rstrip()
s2 = input().rstrip()

# IV, IX = 4, 9
# XL, XC = 40, 90
# CD, CM = 400, 900

ara = 0
def convert(ss):
    tmp = 0
    for i in range(len(ss)):
        tmp += ta[ss[i]]
        if i < len(ss) - 1:
            if ta[ss[i]] < ta[ss[i+1]]:
                if ss[i:i+2] in ma:
                    tmp += (ma[ss[i:i+2]] - ta[ss[i]] - ta[ss[i + 1]])
        
    return tmp

ara += convert(s1)
ara += convert(s2)

print(ara)
rome = []
if ara >= 1000:
    rome.append('M' * (ara // 1000))
    ara %= 1000

if ara >= 900:
    rome.append('CM')
    ara -= 900

if ara >= 500:
    rome.append('D' * ( ara // 500))
    ara %= 500

if ara >= 400:
    rome.append('CD')
    ara -= 400

if ara >= 100:
    rome.append('C' * (ara // 100))
    ara %= 100

if ara >= 90:
    rome.append('XC')
    ara -= 90

if ara >= 50:
    rome.append('L' * (ara // 50))
    ara %= 50

if ara >= 40:
    rome.append('XL')
    ara -= 40


if ara >= 10:
    rome.append('X' * (ara // 10))
    ara %= 10

if ara >= 9:
    rome.append('IX')
    ara -= 9
    
if ara >= 5:
    rome.append('V' * (ara // 5))
    ara %= 5

if ara >= 4:
    rome.append('IV')
    ara -= 4

if ara >= 1:
    rome.append('I' * (ara // 1))
    
print(''.join(rome))