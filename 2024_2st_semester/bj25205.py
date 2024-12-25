import sys
input = sys.stdin.readline
#   ㄱ,ㄲ,ㅅ,ㄴ,ㅈ,ㅎ,ㄷ,ㄹ,ㅁ,ㅂ,ㅌ,ㅍ,ㅆ,ㅇ,ㅊ,ㅋ    
ma = ['r', 'R', 't', 's', 'w', 'g', 'e', 'f', 'a', 'q','x','v','T','d','c','z']
n = int(input())
s = input().rstrip()


if s[-1] in ma:
    print(1)

else:
    print(0)