'''
* 리스트(list)
- 리스트는 여러 개의 값을 집합적으로 저장하기 위해 사용하는 파이썬의 자료형입니다.
- 다른 언어의 배열과 유사한 개념이며, 실제로 배열과 유사한 방식으로 데이터가 관리됩니다.
- [](대괄호) 안에 요소를 콤마로 구분하여 나열합니다.
'''

x = [5, 6, 13, 'a']     # 자바는 같은 타입만 가능하지만, 파이썬은 다른타입 객체들 담을 수 있다. (자바의 Object처럼.)
                        # 그래도 보통은 같은 타입으로 담아준다.
print(type(x)) # : <class list>

for c in x :
    print(c)

print('리스트의 길이 : ', len(x))