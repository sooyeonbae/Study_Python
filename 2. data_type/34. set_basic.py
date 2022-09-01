# 자료형 set  (자바에도 있는 자료형이다.)
'''
* 집합 (set)
- 집합은 여러 값들의 모임이며, (index 없음)
    저장 순서가 보장되지 않고 중복값의 저장을 허용하지 않습니다. (list는 중복값 허용 가능. index로 구분이 가능하니까.)
- 집합은 사전과 마찬가지로 {}로 표현하지만, 
    key : value 쌍이 아닌, 데이터가 하나씩 들어간다는 점이 사전과는 다릅니다.
- set() 함수는 공집합을 만들기도 하며, 다른 컬렉션 자료형을 집합형태로 변환할 수도 있습니다.

만드는법
# []-list(), tuple()(소괄호로만 만들수없음), {}-dict(), set()(중괄호로만 만들수없음) 
'''

names = {'홍길동', '김철수', '박영희', '고길동', '홍길동'}
print(type(names)) # : <class 'set'>

print(names) # : {'홍길동', '박영희', '김철수', '고길동'} 중복순서보장X, 중복된 값 하나만 출력된다.

# 반복문
for x in names :
    print(x)

# 김철수만 꺼내기 (인덱스가 없어서 이런식으로 해야한다.)
for x in names :
    if x == '김철수' :
        print(x)
        break

# 내장함수 set()으로 공집합 만들기
s = set()
print(type(s))
print(s) # : set()      {} : 비어있는 사전



s1 = 'programming'
print(set(s1))      # : {'m', 'p', 'g', ...} 중복값도 다 걸러지고 순서도 안지켜짐
print(list(s1))     # : ['p', 'r', 'o', ...]
print(tuple(s1))    # : ('p', 'r', 'o', ...)


'''
- 집합은 변경 가능한 자료형이어서 언제든지 데이터를 편집할 수 있습니다.
- 집합에 요소를 추가할 때 : add() 메서드
-           제거     : remove() 메서드
'''

asia = {'korea', 'china', 'japan'}
print(asia)
asia.add('thailand')
asia.add('china')
asia.remove('japan')
print(asia)


# 집합의 결합 : update() 메서드 (덧셈연삼 안됩니다. list,tuple은 되겠지만..)
asia2 = {'singapore', 'indonesia', 'korea'}
# print(asia+asia2)   - error
asia.update(asia2)

print(asia) # : 결합됨(중복값 허용X)
