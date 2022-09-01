'''
* 내장함수 map()
- map()은 첫번째 인수로 함수를 지정하고,
        두번째 인수로 리스트를 지정하면 
        해당 리스트 내부 요소값을 일괄적으로 첫번째 인수로 지정한 함수에 인수로 전달합니다.
'''

# 3개의 숫자 중 최대값을 판별하여 리턴하는 함수를 정의
def max_of_three(n1, n2, n3) :
    if n1 > n2 :
        if n1 > n3 :
            return n1
        else :
            return n3
    else :
        if n2 > n3 :
            return n2
        else :
            return n3

# map() 안 쓴 버전
# n1 = int(input('정수 1 : '))
# n2 = int(input('정수 2 : '))
# n3 = int(input('정수 3 : '))

# map() 버전
n1, n2, n3 = map(int, input('정수 3개를 공백으로 구분해서 입력하세요 : ').split())   # => [정수1(아직 문자열), 정수2, 정수3]을 일괄적으로 int에 대입해서
                                                                            # n1, n2, n3로
print('최대값 : ', max_of_three(n1, n2, n3))




# 세제곱해주는 함수
def triple_square(number) :
    return number**3

li = [2,4,6,8,10]
# 기존 방법
# triple_square(li[0])
# triple_square(li[1])
# triple_square(li[2])
# triple_square(li[3])
# triple_square(li[4])

# map()버전
# li 안에 있는 모든 데이터들을 triple_square 함수로 전달해서
# 값을 변환하기 위해 사용했다.
# map함수가 return 하는 객체를 list로 변환해서 확인하기.
result = list(map(triple_square, li))
print(result)



# map(함수, 리스트) -> 리스트 내부 요소를 함수로 일괄 전달.
# 여러 개의 데이터를 한번에 다른 형태로 변환하기 위해 사용.