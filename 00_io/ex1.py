# 입출력 처리

a = input()
a = int(a)
print(a, type(a))

a = int(input())
print(a, type(a))

a = float(input())
print(a, type(a))


# 정수 2개 입력
# 100
# 200
a = int(input())
b = int(input())
print(a, b)

# 100 200
input().split()
print(a, type(a))

# map(함수, 리스트)
a, b, c = map(int, input().split())
print(a, b, c, type(a))

# 리스트
list(map(int, input().split()))
print(a, type(a))
