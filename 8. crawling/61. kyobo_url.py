from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from datetime import datetime
import codecs

d = datetime.today()
file_path = f'/Users/baesy/Desktop/web_development/Python/crawling/교보 베스트셀러_{d.year}년_{d.month}월_{d.day}일.html'

with codecs.open(file_path, mode='w', encoding='utf-8') as f :
    driver = webdriver.Chrome('/Users/baesy/Desktop/web_development/Python/chromedriver')
    driver.get('http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?orderClick=d79')

    src = driver.page_source
    soup = BeautifulSoup(src, 'html.parser')


    # 책 한 권 관련 태그
    # print('책 한 권 관련 태그 : ', detail_list[0])

    # 책 한 권 관련 a 태그 텍스트 = 제목
    # print('책 한 권 관련 a태그 : ', detail_list[0].find('a').text)


    # 책 한 권 주소
    # print('책 한 권 주소 : ', detail_list[0].find('a'))
    # print('타입 : ', type(detail_list[0].find('a'))) # :  <class 'bs4.element.Tag'>
    # print('문자열로 하는거 먹히나? : ', str(detail_list[0].find('a')))
    # str_html = str(detail_list[0].find('a'))
    # addr = str_html.split('"')[1]
    # print('href만 자르기 : ', addr)
    detail_list = soup.find_all('div', class_='detail')
    rank = 1

    for detail in detail_list :
        title = detail.find('a').text
        str_href = str(detail.find('a'))
        addr = str_href.split('"')[1]

        # href = a_url.get('href') 태그 요소에서 속성 얻어오기.

        f.write(f'순위 : {rank}위')
        f.write('<br>')
        f.write(f'<a href="{addr}"> {title} </a> \n')
        f.write('<hr>')

        rank += 1