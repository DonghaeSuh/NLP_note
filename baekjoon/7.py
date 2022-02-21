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