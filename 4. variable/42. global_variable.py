'''
* 전역변수 (global variable)
- 지역변수가 함수 내부에서만 사용하는 변수라면
    전역변수는 프로그램 전체에서 사용하는 공용변수입니다.
- 파이썬에서는 들여쓰기 없이 선언된 변수를 전역변수로 취급하며,
    전역변수는 함수 내부, 제어문 내부 등 프로그램 어디에서나 사용이 가능합니다.
'''

sale_rate = 0.2  #전역변수(들여쓰기없음)

def calc_price(price) :
    print(f'오늘의 할인율 : {sale_rate * 100}%')

    today_price = price - (price * sale_rate)       #지역변수(calc_price 에서만 유효)
    print(f'오늘의 가격 : {today_price:0.0f}원')

calc_price(2000)

# print(today_price) - error. 지역변수니까


# return 받아서 today_price 받기
def calc_price(price) :
    print(f'오늘의 할인율 : {sale_rate * 100}%')

    today_price = price - (price * sale_rate)       #지역변수(calc_price 에서만 유효)
    print(f'오늘의 가격 : {today_price:0.0f}원')
    return today_price

t_price = calc_price(2000)
print(t_price)