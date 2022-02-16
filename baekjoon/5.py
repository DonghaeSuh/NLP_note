#10818
"""
a=int(input())
b=list(map(int,input().split()))
print(f"{min(b)} {max(b)}")
"""
"""
n=int(input())
L=list(map(int, input().split()))
L.sort()
print(L[0],L[-1])
"""

#2562
"""
r=[]
for i in range(9):
    r.append(int(input()))
print(max(r))
print(r.index(max(r))+1)
"""

#2577
# 곱한것을 list로 형태변환하면 각 숫자는 리스트의 원소로 저장된다. (그러려면 정수 값을 str로 저장해야 함)
# 이후 횟수를 저장할 리스트를 하나 생성해놓고, for 문 2개를 통해 0부터9까지 접근하면서 몇개 있는지를 이 리스트에 저장한다.
"""
a=int(input())
b=int(input())
c=int(input())
s=list(str(a*b*c))
r=[0]*10
for i in range(len(s)):
    for k in range(10):
        if int(s[i])==k:   #s의 원소 값들이 다 str이므로 이때 k는 int 이므로 형태 맞추어 주어야 비교를 할 수 있다.
            r[k]+=1
for p in range(10):
    print(r[p])
"""

# 3052
# 값 비교할 때 for문 2개로 처리 가능
"""
r=[]
for i in range(10):
    r.append(int(input()))
s=[0]*42

for i in range(10):
    for k in range(42):
        if r[i]%42==k:  
            s[k]+=1
cnt=0
for d in range(42):
    if s[d]!=0:
        cnt+=1
print(cnt)
"""

"""
a = [int(input()) for _ in range(10)]
b = [i % 42 for i in a]

print(len(set(b)))
"""



"""
inputs = map(int, [input() for _ in range(10)])

li = list()
for n in inputs:
  r = n % 42
  if r not in li:
    li.append(r)
print(len(li))
"""

#1546
"""
n=int(input())
s=list(map(int,input().split()))
s.sort() # max() 써라 리스트니까

f=[i/s[n-1]*100 for i in s]
r=0
for i in range(n):   # sum() 써라 리스트니까
    r+=f[i]
print(r/n)
"""

#8958
