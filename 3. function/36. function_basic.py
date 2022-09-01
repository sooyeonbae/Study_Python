'''
* 함수 (function)
- 함수는 지속적으로 사용되는 코드 블록에 이름을 붙여놓은 형태입니다.
- 함수는 한 번 정의해두면 지정된 함수 이름을 통해 언제든지 해당 코드 블록을 실행할 수 있습니다. (코드를 모듎화)
- 메서드는 수명이 있지만 (객체의 소멸시) 함수는 수명이 없다.
- 함수를 정의할 때 사용하는 키워드는 def(define 약어) 입니다.
- 정의해 둔 함수를 사용하는 것을 호출(function call)이라고 부릅니다.
- 파이썬에서는 함수를 호출하려면 반드시 호출문보다 '상단부'에 함수를 먼저 정의해야 합니다.
'''

# 함수의 정의 (1~x까지의 누적합을 구하는 로직)
def calc_sum(x) :        # 괄호 안 : 매개변수
    sum = 0
    for n in range(1, x+1) :    # : range는 미만이라 +1
        sum += n
    return sum

# 함수의 호출
print('1~100까지의 누적합 : ', calc_sum(100))


'''
* 인수(=매개변수) (arguments)   (파이썬에서는 '인수'라고 하는 경우가 더 많다)
- 인수는 함수를 호출할 때 함수 실행에 필요한 값들을 전달하는 매개체 역할을 하며,
    그렇기 때문에 매개변수(parameter)라고도 부릅니다.
- 인수의 개수는 제한이 없어 많은 값을 함수에 전달할 수도 있고, 하나도 전달하지 않을 수 있습니다. (권장 : 4개 이하. 그 이상은 리스트나 객체 등등으로 묶어서..)
- 파이썬의 경우에는 타입을 작성하지 않기 때문에
    이 함수를 처음 사용하는 사람도 인수 이름만 보고 무슨 값을 전달해야 할 지 의미를 알기 쉽게 지정하는 것이 좋습니다.
'''


'''
* 연습

1. 인수를 정수형태로 시작값(start), 끝값(end)을 입력받아
 반복문으로 start부터 end까지의 누적 총합을 구하는 함수를 정의하세요.

2. 함수 이름은 calc_rangesum으로 정의하세요.
ex) calc_rangesum(3, 7) -> 3부터 7까지의 누적합을 구해와야 함.

3. 출력예시: "x~y까지의 누적합: z"
사용자에게 입력받은 값을 함수로 전달해서 값을 출력해 보세요.
'''
# 내 코드
def calc_rangesum(start, end) :
    sum = 0
    for n in range(start, end+1) :
        sum += n
    return sum

x = input('첫번째 값 입력하세요 : ')
y = input('두번째 값 입력하세요 : ')
print(f'{x} ~ {y} 까지의 누적합 : ', calc_rangesum(4,5))


# 선생님 코드
# def calc_rangesum(start, end) :
#     if start > end :
#         start, end : end, start #튜플
#     total = 0
#     for n in range(start, end+1) :
#         total += n
#     return total

# n1 = int ('정수 1 :')
# n2 = int ('정수 2 :')
# print(f'{n1} ~ {n2}까지의 누적합 : {calc_rangesum(n1, n2)}')



'''
* 반환값 (return value)
- 반환값이란 함수를 호출한 곳으로 함수의 최종 실행 결과를 전달하는 값입니다.
- 인수는 여러 개 존재할 수 있지만, 반환값은 언제나 하나만 존재해야 합니다.
- 모든 함수가 반환값이 있는 것은 아닙니다.
    함수 실행 후 딱히 반환할 값이 없다면 return을 생략할 수 있습니다. (자바의 void)
'''

def add(n1, n2) :
    return n1+n2

result = add(10, 5)
# 리턴이 있는 함수는 다른 함수의 매개값으로도 사용이 가능합니다.
print(add(add(5,7),add(9,8))) # 리턴값을 다른 함수의 매개값으로 전달이 가능하다. (add(12, 17))

# n = int(input('정수 : ')) -> n = int('3')

def operate_all (n1, n2) :
    return n1+n2, n1-n2, n1*n2, n1/n2 # tuple로 리턴하기
    # return n1-n2
    # return n1*n2
    # return n1/n2         리턴키워드로 탈출도 하기때문에 밑에 return에는 접근이 불가능하다 
    #                      -> (java JS처럼 결과를 list tuple set 등으로 포장해서 리턴하면된다.)

print(type(operate_all(10,5))) # : <class 'tuple'>


def multi (n1, n2) :
    result = n1 * n2
    print(f'{n1} X {n2} = {result}')

multi(9,6)
abc = multi(9,6) # : None (리턴값이 없기때문에)
