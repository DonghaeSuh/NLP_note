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