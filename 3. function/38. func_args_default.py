'''
* 인수의 기본값
- 파이썬에서는 인수의 기본값을 설정하여, 자주 바뀌지 않는 매개값은 기본값으로 처리할 수 있도록 해 줍니다.(JS에서도 가능)
'''

def calc_stepsum(begin, end, step) :
    sum = 0
    for n in range(begin, end+1, step) :
        sum += n
    return sum

print(calc_stepsum(1,10,1))
# print(calc_stepsum(1,10))     -error. 'step'인수가 빠져서.

def calc_stepsum(begin, end, step=1) :  # 이렇게 step=1 로 해두면 전달되지않았을때 1로 들어간다.
    sum = 0
    for n in range(begin, end+1, step) :
        sum += n
    return sum

print(calc_stepsum(2,5))        # step값 안줬으니까 기본값인 1로
print(calc_stepsum(1,20,2))     # step값을 줬으니까 2로


# 기본값 2개 주기 : 기본값 선언하지 않은 애를 맨 왼쪽으로 줘야한다. (기본값이 지정된 인수를 오른쪽으로 몰아주셔야 합니다.)
# def clac_sum (begin=0, end, step=1) :     -error.
def calc_sum (end, begin=0, step=1) :
    sum = 0
    for n in range(begin, end+1, step) :
        sum += n
    return sum

print(calc_sum(100))    # 첫번째 인수로 들어간다.
