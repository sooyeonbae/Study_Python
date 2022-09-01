'''
* 키워드 인수 (keyword argument)
- 인수의 개수가 많아지면 인수의 순서를 파악하기 어렵고
    함수를 호춣할 때 전달할 값의 위치를 헷갈릴 가능성이 높아집니다.
ex) def signup_user(id, pw, name, addr, email, phone ... )

- 파이썬에서는 순서와 무관하게 인수를 전달할 수 있는 방법을 제공하여
    인수의 이름을 직접 지정하여 값을 전달하는 키워드 인수 방식을 제공합니다.
'''

def calc_sum(begin, end, step) :
    sum = 0
    for n in range(begin, end+1, step) :
        sum += n
    return sum

# 일반적인 함수 호출 (위치 인수 방식 (positional argument))
calc_sum(3, 7, 1)

# 키워드 인수 사용 (순서 상관 x)
print(calc_sum(begin=3, step=1, end=7))
print(calc_sum(step=2, end=9, begin=2))

# 위치인수와 키워드인수의 혼합사용시에는
# 무조건 위치인수가 앞에 와야합니다.
print(calc_sum(3, step=1, end=7))
            # 3: begin

# print(calc_sum(end=7, 3, 1))      -error. 키워드인수는 위치인수보다 뒤에 가야한다.

# print(calc_sum(3, 1, end=7))      -error. 두번째값이 end로 간다. ->end가 두개 들어가고 step 값이 안들어가게됨.

# print(clac_sum(3, end=7, 1))      -error. 키워드인수가 위치인수보다 뒤에 가야한다.


print(3, 6, 9, sep='->', end='!')   # print함수의 키워드인수방식이다. 
                                # (sep, end 순서는 바뀌어도 되지만 sep, end(키워드인수)가 위치인수보다 앞에가면안된다.)

                                
