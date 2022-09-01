# 1위~50위 - 파일로 뽑아내기

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
# 날짜표현모듈 (module 폴더 - 60. datetime_basic.py)
from datetime import datetime
# 인코딩모듈    (open함수 쓸 때 codecs.open,   인수에 mode='w', encoding='utf-8')
import codecs


d = datetime.today()

file_path = f'/Users/baesy/Desktop/web_development/Python/crawling/알라딘 베스트셀러 1~50위_{d.year}_{d.month}_{d.day}.txt'


'''
finally 쓰지 않아도 자동으로 close - with       (java의 try with resource와 비슷)
- with문을 사용하면 with 블록을 벗어나는 순간
객체가 자동으로 해제됩니다.
- with 작성시 사용할 객체의 이름을 as 뒤에 작성해줍니다.
'''

'''
* 표준 모듈 codecs
- 웹이나 다른 프로그램의 텍스트 데이터와
파이썬 내부의 텍스트 데이터의 인코딩 방식이 서로 다를 경우에
내장함수 open()이 제대로 인코딩을 적용할 수 없어서 에러가 발생합니다. (UnicodeEncodeError)
- 파일 입/출력시 인코딩코덱을 변경하고싶다면
codecs 모듈을 사용합니다.
'''



with codecs.open(file_path, mode='w', encoding='utf-8') as f :            # with 안썼을 때의 f = open(file_path, 'w') :
    driver = webdriver.Chrome('/Users/baesy/Desktop/web_development/Python/chromedriver')
    driver.get('https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1&start=we')

    # 순위 표시 변수
    rank = 1

    # 소스코드 전부 끌고오기
    src = driver.page_source

    # 뷰슾 객체생성
    soup = BeautifulSoup(src, 'html.parser')   

    # 데이터 잘라오기 (반복문)

    div_list = soup.find_all('div', class_='ss_book_box')
    for div in div_list :
        book_info = div.find_all('li')

        # 증정품이 있는 경우 : 제목이 [1]부터 시작, ss_ht1 있음
        #       없는 경우 :        [0]
        if book_info[0].find('span', class_='ss_ht1') == None :          # find() : 1개 찾기, find_all() : 모두 찾기
                                                    # 찾으면 문자열을 주지만, 못찾으면 None타입 반환된다. -> 증정품 없음
            print(f'{rank}위 - 증정품 없음')
            book_title = book_info[0].text
            book_author = book_info[1].text
            book_price = book_info[2].text
        else :
            print(f'{rank}위 - 증정품 있음')
            book_title = book_info[1].text
            book_author = book_info[2].text
            book_price = book_info[3].text

        auth_info = book_author.split('|')

        f.write(f'# 순위 : {rank}위 \n')
        f.write(f'# 제목 : {book_title} \n')
        f.write(f'# 저자 : {auth_info[0]} \n')
        f.write(f'# 출판사 : {auth_info[1]} \n')
        f.write(f'# 출판일 : {auth_info[2]} \n')
        f.write('# 가격 : ' + book_price.split(', ')[0] + '\n')
        f.write('- ' * 20 + '\n')

        rank += 1
