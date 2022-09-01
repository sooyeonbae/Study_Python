from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from bs4 import BeautifulSoup
import xlsxwriter
from selenium.webdriver.chrome.options import Options
from io import BytesIO
import urllib.request as req

d = datetime.today()
file_path = f'/Users/baesy/Desktop/web_development/Python/crawling/멜론일간차트 1~100위_{d.year}_{d.month}_{d.day}.xlsx'

workbook = xlsxwriter.Workbook(file_path)
worksheet = workbook.add_worksheet()

browser = webdriver.Chrome('/Users/baesy/Desktop/web_development/Python/chromedriver')
browser.get('https://www.melon.com/chart/day/index.htm')
browser.implicitly_wait(5)

# 컬럼 크기
worksheet.set_default_row(50)
worksheet.set_column('A:E', 25)

cell_format = workbook.add_format({'bold':True, 'font_color' : 'red', 'bg_color' : 'yellow'})
worksheet.write('A1', '순위', cell_format)
worksheet.write('B1', '앨범커버', cell_format)
worksheet.write('C1', '노래제목', cell_format)
worksheet.write('D1', '가수', cell_format)
worksheet.write('E1', '앨범명', cell_format)

row_cnt = 2             # 엑셀의 행 수 카운트 (1행은 분류제목이니까)

soup = BeautifulSoup(browser.page_source, 'html.parser')


    for song_tr in song_tr_list :

        # 순위찾기
        rank = song_tr.select_one('div.wrap.t_center').text.strip()
        print('순위 : ' + rank)

        # 이미지찾기
        img_tag = song_tr.select_one('div.wrap > a > img')
        img_url = img_tag['src'
        print('이미지 : ', img_url)

        # 가수 이름
        artist_name = song_tr.select_one('div.wrap div.ellipsis.rank02 > a').text.strip()
        print('가수이름 : ', artist_name)

        