# 내 코드 - 망함  (선생님거보자)


# 순위, 커버사진, 노래제목, 가수이름, 앨범이름
# https://www.melon.com/chart/day/index.htm

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
file_path = f'/Users/baesy/Desktop/web_development/Python/crawling/멜론 차트 1~100위_{d.year}_{d.month}_{d.day}.xlsx'

workbook = xlsxwriter.Workbook(file_path)
worksheet = workbook.add_worksheet()

chrome_option = Options()
chrome_option.add_argument('--headless')
driver = webdriver.Chrome('/Users/baesy/Desktop/web_development/Python/chromedriver', options=chrome_option)

driver.get('https://www.melon.com/chart/day/index.htm')

cell_format = workbook.add_format({'bold':True, 'font_color' : 'red', 'bg_color' : 'yellow'})

worksheet.write('A1', '순위', cell_format)
worksheet.write('B1', '앨범커버', cell_format)
worksheet.write('C1', '노래제목', cell_format)
worksheet.write('D1', '가수', cell_format)
worksheet.write('E1', '앨범명', cell_format)

rank = 1            # 순위
cnt = 2             # 엑셀의 행 수 카운트 (1행은 분류제목이니까)


soup = BeautifulSoup(driver.page_source, 'html.parser')
song_list = []
song_list1 = soup.find_all('tr', class_='lst50')
song_list2 = soup.find_all('tr', class_='lst100')
song_list.append(song_list1)
song_list.append(song_list2)

    
# print('앨범커버 : ', song_list1[0].select_one('img'))
# print(type(song_list1[0].select_one('img')))    # <class 'bs4.element.Tag'>
# print('앨범커버 src : ', song_list1[0].select_one('img')['src'])
# print('노래제목 : ', song_list[0].find_all('a')[2].text)
# print('가수 : ', song_list[0].find_all('a')[3].text)
# print('앨범명 : ', song_list[0].find_all('a')[4].text)
    


for song in song_list:

    # 앨범커버
    # album_cover = song.select_one('div.wrap > a > img')
    album_cover = song.select_one('img')
    img_url = album_cover['src']
    print('img_url : ', img_url)


    song_info = song.find_all('a')

    # 노래제목
    song_title = song_info[2].text
    # print('song_title : ', song_title)

    # 가수
    singer = song_info[3].text
    # print('singer : ', singer)

    # 앨범명
    album = song_info[5].text
    # print('album : ', album)


    # 이미지 바이트로처리
    try :
        album_image = BytesIO(req.urlopen(album_cover['src']).read())
        worksheet.insert_image(f'B{cnt}', 'album_cover', {'image_data' : album_image, 'x_scale':0.5, 'y_scale':0.5})
    except :
        print('이미지 처리 오류')

    worksheet.write(f'A{cnt}', f'{cnt}위')
    worksheet.write(f'C{cnt}', song_title)
    worksheet.write(f'D{cnt}', singer)
    worksheet.write(f'E{cnt}', album)

    cnt += 1
    rank += 1


print('크롤링 끝')

driver.close()
workbook.close()
