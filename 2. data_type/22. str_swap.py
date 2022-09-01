# replace : 대체 (새 문자로)
# swap : 형태를 변경

'''
* 문자열 알파벳 형태 변경 메서드
1. lower() : 영문 알파벳을 모두 소문자로 변경   (자바 : toLowerCase())
2. upper() :                대문자        (자바 : toUpperCase())

3. swapcase() : 영문 대문자를 각각 반대로 변경
4. capitalize() : 문장의 맨 첫글자만 대문자, 나머지는 소문자.
5. title() : 각 단어의 맨 첫글자만 대문자, 나머지는 소문자. (단어의 기준 : 공백)
'''

s = 'GooD MoRnInG ~~~~. my name is BAE. hellO worlD.'
print(s)
print(s.lower())
print(s.upper())
print(s.swapcase)
print(s.capitalize())
print(s.title)