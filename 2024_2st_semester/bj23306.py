import sys
input = sys.stdin.readline
# 제일 처음와 끝을 안다면 가능 
# 처음 0 끝이 1이라면 무슨짓을 해도 오르막길이 더 많다.
# 처음 1 끝이 0이라면 무슨직을 해도 내리막길이 더 많다.
# 예시 4개에 양끝 0, 0 이라면 
# 0000, 0010, 0100, 0110
# 같음, 같음, 같음, 같음

#시간 복잡도: O(1)
n = int(input())

print("? 1")
sys.stdout.flush()
a = int(input())
print(f"? {n}")
sys.stdout.flush()
b = int(input())


if a == 0 and b == 1:
    print("! 1")
elif a == 1 and b == 0:
    print("! -1")
else:
    print("! 0")