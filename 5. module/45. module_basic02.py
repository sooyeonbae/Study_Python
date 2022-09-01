# import의 다양한 방식


# 모듈 내에 존재하는 변수, 함수, 클래스 등을 직접 임포트하는 방법 - 'from 모듈 import 기능'

from math import factorial, gcd      # -> math.factorial() 말고    factorial()로 바로 사용 가능.
                            # gcd : 최대공약수 구해주는 기능
print(factorial(5))
print(gcd(24, 18))


# import할 모듈에 별칭을 지정하여 사용하기 - 'as 별칭'
import statistics as st

li = [34, 55, 12, 56, 33, 22, 99]
# 별칭붙이기 전
# print('평균 : ', statistics.mean(li))
# print('분산 : ', statistics.variance(li))
# print('표준편차 : ', statistics.stdev(li))

# 별칭 붙인 후
print('평균 : ', st.mean(li))
print('분산 : ', st.variance(li))
print('표준편차 : ', st.stdev(li))



# 위에서 알려드린 두 가지 개념을 합쳐서도 사용이 가능합니다.
from math import factorial as fac
print(fac(4))
