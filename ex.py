"""A= list(input())
r=int(A[0])+int(A[2])
print(r)"""

"""
A= input()
r=int(A[0])+int(A[2])
print(r)

"""

"""
a,b=map(int,input().split())
print(a+b)
"""

"""
a,b=map(int,input().split())
print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
print(a%b)
"""

"""
id = input()
if id=="joonas":
    print("joonas??!")
"""

"""
print((lambda x : x-543)(int(input())))
"""

"""
A,B,C= map(int,input().split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)
"""
"""
a=int(input())
b=input()
print(a*int(b[2]))
print(a*int(b[1]))
print(a*int(b[0]))
print(a*int(b))

"""


a,b=map(int,open(0))
print(b%10*a,b%100//10*a,b//100*a,b*a)
