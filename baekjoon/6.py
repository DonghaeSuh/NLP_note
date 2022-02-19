#15596
"""
def solve(a):
    ans = sum(a)
    return ans
"""

#4673
#셀프넘버
# 셀프 넘버가 아닌 것들의 리스트 생성 => 이후 여집합을 이용
# 각 숫자마다 리스트형태 변환하고, '리스트 sum+ 현재숫자' 
"""
r=set()
for i in range(1,10001):
    a= list(str(i))
    a_=[int(i) for i in a]
    s=i+sum(a_)
    r.add(s)
f=list(set(range(1,10001))-r)
f.sort()
for k in range(len(f)):
    print(f[k])
"""

#1065
#정수 받고, 
# 일단 1부터 99까지는 한수
# 3자리 이상부터 사이에 있는 값의 2배가 양쪽을 둘러싸고 있는 두 수의 합과 같으면 count
"""
a=int(input())

if a<100:
    print(a)
else:
    c=0
    for j__ in range(100,a+1):
        j_=list(str(j__))
        j=[int(k) for k in j_]
        for l in range(len(j)-2):
            if j[l]+j[l+2]==j[l+1]*2:
                c+=1
    if a==1000:
        print(99+c-1)
    else:
        print(99+c)
"""

"""
n = int(input())
if n < 100:
    print(n)
else:
    count = 99
    for i in range(100, n+1):
        a = i // 100
        b = (i % 100) // 10
        c = i % 10
        if (b - a) == (c - b):
            count += 1
        print(count)
"""