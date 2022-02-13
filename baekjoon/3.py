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



