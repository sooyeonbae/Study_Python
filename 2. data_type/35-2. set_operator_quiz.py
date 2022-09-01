'''
- 서로 다른 정수가 담김 두 개의 리스트를 비교하여
li 안에 있는 정수가 li2에도 담겨있다면 그 정수를 배제하시고
서로 겹치지 않는 정수만 담긴 새로운 리스트를 생성해보세요.
'''

# 내 풀이
li1 = [1,2,3,4,5,6,7]
li2 = [1,3,8,4,5,7,101]

s1 = set(li1)
s2 = set(li2)

li3 = s1^s2
li = list(li3)
print(li)


# 선생님 코드 (list만 쓴 버전)
li3 = []
for n in li1 :
    if n not in li2 :
        li3.append(n)
for n in li2 :
    if n not in li1 :
        li3.append(n)
li3.sort()
print(li3)

# 선생님 코드 (set 버전)
result = set(li1) ^ set(li2)
print(result)