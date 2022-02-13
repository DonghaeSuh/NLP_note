# 2739
"""
a=int(input()) 
for i in range(1,10):
    print("{} * {} = {}".format(a,i,i*a))  # print(f'{a} * {i} = {a*i}')
"""
# 10950
"""
l = range(int(input()))
result =[]
for i in l:
    a,b=map(int,input().split())
    result.append(a+b)
for w in l:
    print(result[w])
"""

"""
입력을 다 받고 한꺼번에 출력해야 하는 줄 알앗으나 아니였음
t = int(input())

for result in range(t):
    A, B = map(int, input().split())
    print(A+B)

"""
# 8393
"""
a= int(input())
b=0
for i in range(a):
    b+=i+1
print(b)
"""

#15552

#+ .rstrip() test
"""
import sys
test =[]
a= sys.stdin.readline()
test.append(a.rstrip())
b= sys.stdin.readline()
b.rstrip()
test.append(b)
print(test)
"""
"""
import sys
r=int(sys.stdin.readline().rstrip())
for i in range(r):
    a,b=map(int,sys.stdin.readline().split())
    print(a+b)
"""

#2741
"""
import sys
r=int(input())
for i in range(r):
    print(i+1)
"""
"""
[print(i) for i in range(1, int(input())+1)]
"""

#2742
"""
r=int(input())
for i in range(r):
    print(r-i)
"""

#11021
"""
r=int(input())
for i in range(r):
    a,b=map(int,input().split())
    print(f"Case #{i+1}: {a+b}")
"""

#11022
"""
r=int(input())
for i in range(r):
    a,b=map(int,input().split())
    print(f"Case #{i+1}: {a} + {b} = {a+b}")
"""


#2438
"""
r=int(input())
for i in range(r):
    for k in range(i+1):
        print('*',end="")
    print()
"""

#2439
"""
r=int(input())
for i in range(1,r+1):
    for j in range(r-i):
        print(" ",end="")
    for l in range(i):
        print('*',end="")
    print()
"""

"""
출력에서 "문자열"*반복횟수  가 가능하다.
n = int(input())
for i in range(1, n+1):
    print(" " * (n - i) + "*" * i)
"""

#10871
r,x=map(int,input().split())
a=input().split()   #a = list(map(int, input().split())) 로 하면, list 내부의 원소 값이 정수일 경우 인식 가능
for i in range(r):
    if int(a[i])<x:
        print(a[i],end=" ")
        