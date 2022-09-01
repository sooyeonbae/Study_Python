# 페이지 이동하면서 1~400위까지 긁어오기

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
# 날짜표현모듈 (module 폴더 - 60. datetime_basic.py)
from datetime import datetime
# 인코딩모듈    (open함수 쓸 때 codecs.open,   인수에 mode='w', encoding='utf-8')
import codecs


d = datetime.today()

file_path = f'/Users/baesy/Desktop/web_development/Python/crawling/알라딘 베스트셀러 1~400위_{d.year}_{d.month}_{d.day}.txt'


with codecs.open(file_path, mode='w', encoding='utf-8') as f :            # with 안썼을 때의 f = open(file_path, 'w') :
    driver = webdriver.Chrome('/Users/baesy/Desktop/web_development/Python/chromedriver')
    driver.get('https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1&start=we')

    '''
    XPath
    1위~ //*[@id="newbg_body"]/div[3]/ul/li[2]/strong
        //*[@id="newbg_body"]/div[3]/ul/li[3]/a
        //*[@id="newbg_body"]/div[3]/ul/li[4]/a
        . . .
        //*[@id="newbg_body"]/div[3]/ul/li[10]/a
    '''

    # 순위 표시 변수
    rank = 1



    for n in range(3, 11) :
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

        driver.find_element(By.XPATH, '//*[@id="newbg_body"]/div[3]/ul/li['+ str(n) +']/a').click()
        time.sleep(1)

