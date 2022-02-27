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
# 집합 이용해 존재하는 단어 뽑아옴, 사전일경우 key같으면 덮어씌어지므로 사용하면 안됨
# 등장 횟수 리스트로 정리한다음 reverse sort했을때, 0번과1번이 같으면 가장 많이 사용된 알파벳이 여러개 존재
# 가장 많이 사용된 알파벳을 대문자로 출력한다고 하니 입력받은 단어 모두 upper해서 해도 됨

"""
a=input().upper()
a_list=list(set(a))

r=[]
for i in range(len(a_list)):
    cnt=0
    for k in range(len(a)):
        if a[k]==a_list[i]:
            cnt+=1
    r.append(cnt)
r_rev=sorted(r,reverse=True)
if len(r)==1:
    print(a)
elif r_rev[0]==r_rev[1]:   # 여기서 실수를 해서 오류 해결하느라
    print("?")
else:
    print(a_list[r.index(r_rev[0])])

"""

"""
words = input().upper()
unique_words = list(set(words))  # 입력받은 문자열에서 중복값을 제거

cnt_list = []
for x in unique_words :
    cnt = words.count(x)
    cnt_list.append(cnt)  # count 숫자를 리스트에 append

if cnt_list.count(max(cnt_list)) > 1 :  # count 숫자 최대값이 중복되면
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
    print(unique_words[max_index])
"""

#1152
"""
a=input().split()
print(len(a))
"""

#2908
"""
a,b=input().split()
a_=reversed(list(a))
b_=reversed(list(b))
a__="".join(a_)
b__="".join(b_)
if (int(a__)<int(b__)):
    print(int(b__))
else:
    print(int(a__))
"""

#5622
#문자열 저장한다음, 순서정보가지고 초계산, 구간 문자 넣음
#구간문자를 세기
"""
a="ABC,DEF,GHI,JKL,MNO,PQRS,TUV,WXYZ"
d=list(input())
r=[]
for i in range(len(d)):
    r.append(a[:a.find(d[i])].count(',')+3) # ,가 몇개 있는지 그에따른 필요 시간
print(sum(r)) 
"""
"""
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
string = input()
time = 0

for i in range(len(dial)):
    for s in string:
        if s in dial[i]:
            time += 3+i

print(time)
"""

#2941
# 긴 단어가 1개로 간주되어야 하므로 1개영역을 차지하는 문자로 바꿔준다.
"""
c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in c :
    word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수
print(len(word))
"""

#1316
#분류를 해야한다.
#처음 문자는 저장하고 슬라이싱하다가 그 다음이 다른문자이면 그 다음문자를 집합에 추가하자
# 집합을 추가 할 때, 이미 집합에 존재하면, 에러가 있는 정보라는 것을 변수에 저장 => 끝나고 에러있는 것은 카운트하지 않음
"""
a=int(input())
c=0
for i in range(a):
    b=input()
    r=set()
    r.add(b[0])
    e=0
    for k in range(len(b)-1):
        if b[k]!=b[k+1]:
            if b[k+1] in r:
                e=1
            else:
                r.add(b[k])
    if e==0:
        c+=1
print(c)
"""
"""
n = int(input())

group_word = 0
for _ in range(n):
    word = input()
    error = 0
    for index in range(len(word)-1):  # 인덱스 범위 생성 : 0부터 단어개수 -1까지 
        if word[index] != word[index+1]:  # 연달은 두 문자가 다른 때,
            new_word = word[index+1:]  # 현재글자 이후 문자열을 새로운 단어로 생성
            if new_word.count(word[index]) > 0:  # 남은 문자열에서 현재글자가 있있다면
                error += 1  # error에 1씩 증가.
    if error == 0:  
        group_word += 1  # error가 0이면 그룹단어
print(group_word)
"""
