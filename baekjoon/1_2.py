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
"""
a,b=map(int,input().split())

if b-45>=0:
    print(str(a)+" "+str((b-45)))
elif a-1>=0:
    print(str(a-1)+" "+str((60+(b-45))))
else:
    print("23 "+str((60+(b-45))))
"""

#2525
# 입력에 따른 집합 선택을 위한 if 문 구성
# 가장 큰 상류는 올림하였을 때, 24를 넘는가 안넘는가 
# 넘는것 걸러내고 남은 것가지고 => 올림계산  + b+m%60을 가지고 올림 계산

"""a,b =map(int,input().split())
m=int(input())

if a+(b+m)//60>=24:
    print(f"{a+(b+m)//60-24} {(b+m)%60}")
else:
    print(f"{a+(b+m)//60} {(b+m)%60}")

#+ 변수 할당을 통한 if 문 줄이기를 통해 단순화 가능
"""

"""
h, m = map(int, input().split())
t = int(input())

m += t
h += m // 60
m %= 60

if h > 23:
  h = h - 24
  
print(h, m)
"""

# 2480
# 3개 받아오고 3개동일 =>2개동일=> 동일없음 순으로 처리
# 여러 조건들이 결합되있는 경우에 대해서는 
# 맨 마지막으로 뺴서 else로 처리하는게 편하다.(이러면 조건 적어줄 필요 없음)

"""
a=list(map(int,input().split()))
r=a[2]*100+a[1]*10+a[0]

if r%111==0:
    print(f"{10000+(r//111)*1000}")
elif a[0]!=a[1] and a[0]!=a[2] and a[1]!=a[2]:
    a.sort()
    print(a[2]*100)
else:
    if a[0]==a[1]:
        print(1000+a[0]*100)
    elif a[0]==a[2]:
        print(1000+a[0]*100)
    else:
        print(1000+a[1]*100)
"""

"""
a, b, c = map(int, input().split())

if a == b and b == c :
    prize = 10000 + a * 1000
elif a == b or c == a :
    prize = 1000 + a * 100
elif b == c :
    prize = 1000 + b * 100
else :
    prize = max(a, b, c) * 100

print(prize)
"""

        