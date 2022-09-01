# 알라딘 사이트 크롤링

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 뷰티풀수프 임포트
from bs4 import BeautifulSoup

# 웹드라이버 활성화 및 알라딘 홈페이지 이동
driver = webdriver.Chrome('/Users/baesy/Desktop/web_development/Python/chromedriver')
driver.get('https://www.aladin.co.kr')
time.sleep(1)

# 베스트셀러 탭 클릭
driver.find_element(By.XPATH, '//*[@id="re_mallmenu"]/ul/li[3]/div/a/img').click()
time.sleep(1.5)

# 셀레늄에게 페이지소스보기 내용 긁어오라고 하고, 필요한 정보영역을 추리기...
# 한 권의 책에 대한 내용 감싸고있는 영역 (td는 안됨) 찾기. : ss_book_box
# 소스보기 가서 ss_book_box 검색 (: 50개 나온다. 여기다!)
# ss_book_box 기준으로 한 권 정보 뜯어오고 나머지는 반복문처리, 탭 옮겨서 다음페이지들거까지 반복문
# 제목, 지은이, 가격 등


# selenium으로 현재 페이지의 html 소스 코드를 전부 불러오기. (셀레늄 할일 끝)
src = driver.page_source
# print(src)


# 뷰티풀 수프 객체 생성 (임포트 미리)
# 뷰티풀수프 객체를 생성하면서, 셀레늄이 가지고 온 html소스코드를 제공하고,
# 해당 소스코드를 html문법으로 변환하라는 주문.
soup = BeautifulSoup(src, 'html.parser')    # 파이썬은 객체생성할때 new 안한다.

'''
- 뷰티풀수프를 사용하여 수집하고싶은 데이터가 들어있는 태그를 부분 추출할 수 있습니다.
- 메서드 종류
find_all() : 인수값으로 추출하고자 하는 태그의 이름을 적으면, 해당 태그만 전부 추출하여 리스트에 담아 대입합니다.
'''

div_list = soup.find_all('div', class_='ss_book_box')       # div태그, class이름이 ss_book_box (클래스뒤에 언더바!!)
# print('div_list에 들어있는 데이터 수 : ', len(div_list))
# print(div_list[0]) # 1위책만 가져와보자.
                    # 뜯어보니 2, 3, 4번째 <li>만 중요

first_book = div_list[0].find_all('li')
# li 안에 필요한 텍스트가 다 있었다. 2,3,4번째 li의 텍스트를 가져와야겠다.

# text : 사용자가 실제로 브라우저에서 확인 가능한 텍스트만을(태그 제외) 추출하여 문자열 형태로 반환합니다.
book_title = first_book[1].text  #두번째인덱스의 텍스트만
book_author = first_book[2].text
book_price = first_book[3].text

print('# 제목 : ', book_title)
print('# 저자 : ', book_author)
print('# 가격 : ', book_price)

# 가져온 데이터 정제 - split()
auth_info = book_author.split('|')

print('# 제목 : ', book_title)
print('# 저자 : ', auth_info[0])
print('# 출판사 : ', auth_info[1])
print('# 출판일 : ', auth_info[2])
print('# 가격 : ', book_price.split(', ')[0])

