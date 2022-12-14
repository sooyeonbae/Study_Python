'''
* 식별자 (identifier)

1. 사용자 정의로 데이터에 이름을 붙인 것.
2. 모듈(파일), 패키지, 변수, 함수, 클래스 등의 이름을 식별자라고 합니다.
3. 식별자 이름은 중복해서 지정할 수 없습니다.
'''

# 식별자 이름을 숫자로 지정하거나 숫자로 시작하면 안됩니다.
# 7 = 777 (X)
# 7number = 7 (X)
number7 = 7
num7ber = 7

# 식별자 이름에 공백 들어가면 안됩니다.
# my birth day = 20120212 (X)
my_birth_day = 20121212 # 스네이크케이스 사용

# 키워드를 식별자로 지정할 수 없습니다. (if, while, for)
# if = '만약에' (X)
IF = '만약에' # (O). 그치만 비추천

# print()와 같은 내장함수의 이름을 식별자로 사용할수는 있지만
# 더이상 함수의 기능을 쓸 수는 없습니다.
print = '출력하다'
# print(print) (X)

# 한글, 한자 등 영어 이외의 문자도 가능하긴하지만
# 사용을 권장하지는 않습니다.
야옹이 = '고양이' # 별로...
print (야옹이)