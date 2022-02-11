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

"""
a,b=map(int,open(0))
print(b%10*a,b%100//10*a,b//100*a,b*a)
"""

"""
a,b=map(int,input().split())
if(a>b):
    print(">")
elif a<b:
    print("<")
else:
    print("==")
"""


"""
a=int(input())
if 90<=a<=100:
    print("A")
elif 80<=a<90:
    print("B")
elif 70<=a<80:
    print("C")
elif 60<=a<70:
    print("D")
else:
    print("F")
"""

#2753
"""
a=int(input())
if a%4==0:
    if a%100 ==0:
        if a%400==0:
            print(1)
        else:
            print(0)
    else:
        print(1)
else:
    print(0)
"""


#14681
"""
a=int(input())
b=int(input())
if(a>0):
    if b>0:
        print(1)
    else:
        print(4)
else:
    if b>0:
        print(2)
    else:
        print(3)
"""


#2884
a,b=map(int,input().split())

if b-45>=0:
    print(str(a)+" "+str((b-45)))
elif a-1>=0:
    print(str(a-1)+" "+str((60+(b-45))))
else:
    print("23 "+str((60+(b-45))))
