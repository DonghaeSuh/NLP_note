#11654
"""
print(ord(input()))
"""

#11720
"""
r=int(input())
a=list(input())
a=[int(i) for i in a]
print(sum(a))
"""

#10809
#아스키 코드와(a-z : 97-122), .find()이용
"""
a=input()
r=[]
for i in range(97,123):
    r.append(str(a.find(chr(i))))
f=" ".join(r)
print(f)
"""

#2675

# enter를 주의하자(for문에서는 항상 생각)
"""
a=int(input())
for i in range(a):
    n,l=map(str,input().split())
    for k in range(len(l)):
        for j in range(int(n)):
            print(l[k],end="")
    print()    
"""

"""
t = int(input())
for i in range(t):
    num, s = input().split()
    text = ''
    for i in s:
        text += int(num) * i
    print(text)
"""

#1157
# 집합 이용해 존재하는 단어 뽑아옴, 사전형태도 가능(enumerate 이용)
# 등장 횟수 리스트로 정리한다음 sort했을때, 0번과1번이 같으면 가장 많이 사용된 알파벳이 여러개 존재
# 가장 많이 사용된 알파벳을 대문자로 출력한다고 하니 입력받은 단어 모두 upper해서 해도 됨
a=input().upper()
a_set=set(a)
for i in range(len(a_set)):
    cnt=0
    for k in range(len(a)):
        a[k]==a_set(i)
        cnt+=1
    