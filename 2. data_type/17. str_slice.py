# 자바의 substring()
'''
* 문자열 슬라이싱
- 문자열 인덱싱이 단일 문자를 취할 때 사용했다면
슬라이싱은 문자열 내부의 데이터를 범위를 지정해서 부분추출할 때 사용하는 방법입니다.

ex)
문자열데이터 [begin : end : step]

- range 함수처럼 시작 인덱스는 포함이지만(>=),
끝 인덱스는 포함하지 않습니다.(<)
'''

s = 'python'
print(s[2:5:1]) # : tho
print(s[1:4]) # : yth   step생략시 1로 처리됩니다.
print(s[3:]) # : hon    end를 쓰지않으면 '끝까지'
print(s[:4]) # : pyth   begin을 쓰지 않으면 '처음부터'
print(s[:]) # : python  처음부터 끝까지. print(s)랑 같음.

week = '월화수목금토일'
print(week[::2]) # : 월 수 금 일    처음부터 끝까지, step은 2
print(week[1:6:2]) # : 화 목 토