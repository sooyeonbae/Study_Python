# java의 맵
'''
* 사전 (Dictionary)
- 사전은 키(key)와 값(value)의 쌍을 저장하는 대용량의 자료구조.
- 사전은 타 언어에서는 Map이라고도 부르며 연관배열이라고도 부릅니다.
- 사전을 정의하는 기호는 {}이고, 괄호 안에 데이터를 key : value 형태로 나열하여 저장합니다.
'''

students = {'멍멍이' : '김철수', '야옹이' : '홍길동', '깩꾸쇠' : '둘리'}
print(type(students)) # : <class 'dict'>
print(len(students)) # : 3

'''
- 사전에 사용되는 key값은 중복값을 가질 수 없고, 변경도 안됩니다.
    변경하려면 기존 key를 삭제하고 새로운 key를 넣어야합니다.
- 반면에 value값은 중복을 허용하고, 데이터를 자유롭게 편집할수도 있습니다.
- 사전 내부에 저장된 데이터를 검색할 때는 인덱스대신 key를 사용합니다. (sequence(순차적) 자료형이 아닙니다.)
'''

print(students['멍멍이'])   # : 김철수
print(students['짹잭이'])
# 키를 잘못주면 에러난다.
# print(students['뚝딱이']) (X)

# in 키워드를 사용하여 key의 존재 유무를 파악할 수 있습니다.
print('멍멍이' in students) # : True
print('뚝딱이' in students) # : False