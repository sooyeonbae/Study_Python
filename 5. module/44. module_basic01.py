'''
* 모듈 임포트
- 모듈은 파이썬 코드를 작성해놓은 스크립트 파일이며 (.py)
    모듈 안에는 변수, 함수, 클래스 등이 정의되어 있습니다.
- 파이썬에서는 주요기능들을 표준 모듈로 구성하여
    표준 라이브러리로 제공하고 있습니다. (파이썬 표준 라이브러리 - docs.python.org)
- 표준 모듈이나 외부 모듈을 현재 모듈로 불러와서 사용할 때는
    import 라는 키워드를 사용합니다.
'''

import math

print(5 * 5 * math.pi)      # math에서 pi값 제공함.
print(math.sqrt(3))         # math에서 루트값 제공함
print(math.factorial(6))    # 6팩토리얼
print(math.log10(2))
print(math.log(3,4))
print(math.pow(7,4))        # 7의 4제곱