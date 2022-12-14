'''
* 표준 모듈 datetime
- 운영체제의 현재 시간과 날짜 정보를 파이썬 내부로 읽어오는 기능을 제공하는 모듈입니다. 
(그냥 time : 700101이 기준, datetime : 운영체제의 현재시간)
'''

from datetime import datetime

# 오늘 날짜와 현재 시간 정보를 가지고 있는 객체 리턴
d = datetime.today()
print(d)    # : 2022-07-06 12:11:50.882890

print (f'지금은 {d.year}년 {d.month}월 {d.day}일 {d.hour}시 {d.minute}분 {d.second}초 입니다.')
