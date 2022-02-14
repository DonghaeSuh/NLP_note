#10952
"""
while(1):
    a,b=map(int,input().split())
    if a==0 and b==0:
        break
    print(a+b)
"""

#10951
"""
while(1):
    try:
        a,b=map(int,input().split())
        print(a+b)
    except:
        break
"""

#1110
# 입력받고 합한다음 => 처리해서 나온 새로운 수=> 판단=> 서로 다르면 카운트 ....
# 판단 과정에서 다음  입력받은 수와 같다면 exit 
# 몇번 처리했는지가 관건=> 처리하자마자 카운트
"""
a=int(input())
r=[]
r.append(a)
c=0
while(1):
    r.append((r[c]//10+r[c]%10)%10+(r[c]%10)*10)
    c+=1
    if r[c]==r[0]:
        print(c)
        break
"""
    
"""
numb = int(input())
init = numb
count = 0 

while True:
    a = numb // 10
    b = numb % 10
    c = (a+b) % 10
    numb = (b*10) + c
    count = count +1
    if numb == init:
        break
print(count)    
"""