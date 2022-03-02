#1712
"""
a,b,c = map(int,input().split())

if b >= c:  # 가변비용이 노트북 가격보다 같거나 크면
    print(-1)
else:
    print(a//(c-b)+1)
"""

#2292
#1,6,12,18,24
#1+6(1+2+3+...+n) 
"""
a=int(input())
i=0
while(1):
    if 1+6*(i*(i+1)/2)<a<1+6*((i+1)*(i+2)/2):
        print(i+2)
        break
    i+=1
"""
"""
n = int(input())

nums = 1  # 벌집의 개수, 1개부터 시작
cnt = 1
while n > nums :
    nums += 6 * cnt  
    cnt += 1  
print(cnt)
"""

#1193
#2,3,4,5.. 대각선 합이 이래 늘어남.
# while이용해 푼다.
"""
n=int(input())
c=1
num=1
while(n>num):
    c+=1
    num=(c)*(c+1)/2
if (c)%2 ==0:
    print(round(c-(num-n)),'/',round(1+(num-n)),sep="")
else:
    print(round(1+(num-n)),'/',round(c-(num-n)),sep="")
"""
"""
n = int(input())
i = 1
while n > i:
    n -= i
    i +=1
    
if i % 2:
    print(i+1-n, '/', n, sep = '')
else:
    print(n, '/', i+1-n, sep = '')
"""

#2869
#낮이 밤보다 1 많다.
"""
import sys
a,b,c=map(int,sys.stdin.readline().split())
d=1
while (a*d-b*(d-1))<c:
    d+=1
print(d)
"""
a,b,v = map(int,input().split())
k = (v-b)/(a-b)
print(int(k) if k == int(k) else int(k)+1)