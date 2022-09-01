# 가져온 정보 엑셀로

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from bs4 import BeautifulSoup

# 엑셀 연동 라이브러리 - pip3 install XlsxWriter
# 엑셀 처리 모듈 임포트
import xlsxwriter

# user-agent 정보를 변환해주는 모듈 임포트
# 특정 브라우저로 크롤링을 진행할 때 차단되는 것을 방지
# from fake_useragent import UserAgent

# 요청 헤더 정보를 꺼내올 수 있는 모듈 (기본제공모듈)
import urllib.request as req

# 웹브라우저 안뜨고 크롤링할수있게하는 모듈
from selenium.webdriver.chrome.options import Options

# 이미지를 바이트로 변환처리하는 모듈
from io import BytesIO






d = datetime.today()
file_path = f'/Users/baesy/Desktop/web_development/Python/crawling/알라딘 베스트셀러 1~400위_{d.year}_{d.month}_{d.day}.xlsx'
                                                                                                                    # 엑셀확장자로!
'''
# User Agent 정보 (봇프로그램 정보) 변환 (필수는 아니에요.) - 
# 터미널에서 pip3 install fake_useragent, 위에서 모듈 임포트 먼저
opener = req.build_opener()  # 요청 헤더 정보를 초기화
# 요청헤더에 넣을 정보 담기
opener.addheaders = [('User-agent', UserAgent().chrome)]   # random : 아무 유저에이전트 가져오기 - 브라우저정보
                                                        # (다른거 : ie, opera, chrome, firefox, safari 등등)
# 새로운 헤더 정보를 삽입
req.install_opener(opener)
'''
# 엑셀 처리 선언
# Workbook 객체를 생성하여 엑셀 파일을 하나 생성 (매개값으로 저장될 경로를 지정.)
workbook = xlsxwriter.Workbook(file_path)

# 워크시트 생성
worksheet = workbook.add_worksheet()

# 크롤링 할 때 브라우저 안뜨게하기
chrome_option = Options()
chrome_option.add_argument('--headless')    # 인수로 아무것도 안주면 그냥 브라우저 뜬다.

# 브라우저 설정 (일반모드)
# driver = webdriver.Chrome('/Users/baesy/Desktop/web_development/Python/chromedriver')

# 브라우저 설정 (headless 모드)
driver = webdriver.Chrome('/Users/baesy/Desktop/web_development/Python/chromedriver', options=chrome_option)

# 브라우저 사이즈 조정 (픽셀단위)
driver.set_window_size(800, 600)

# 브라우저 내부 대기 (초 단위)
# time.sleep(10) -> 브라우저 로딩에 상관없이 무조건 10초 대기

# 웹 페이지 전체가 로딩 될 때 까지 대기 후 남은 시간은 무시 (초 단위) - 로딩완료되면 10초 안돼도 그냥 넘어간다.
driver.implicitly_wait(10)

# 페이지 이동 (베스트셀러페이지로)
driver.get('https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1&start=we')

# 엑셀에 텍스트를 저장하기 위해 미리 컬럼 세팅 (인수로 딕셔너리 전달)
cell_format = workbook.add_format({'bold':True, 'font_color' : 'red', 'bg_color' : 'yellow'})

# 글자 쓰기 (인수로 디자인까지전달)
worksheet.write('A1', '썸네일', cell_format)
worksheet.write('B1', '제목', cell_format)
worksheet.write('C1', '작가', cell_format)
worksheet.write('D1', '출판사', cell_format)
worksheet.write('E1', '출판일', cell_format)
worksheet.write('F1', '가격', cell_format)
worksheet.write('G1', '링크', cell_format)

cur_page_num = 2    # 현재 페이지 번호 (XPath에 활용할 값)
target_page_num = 9 # 목적지 페이지 번호
rank = 1            # 순위
cnt = 2             # 엑셀의 행 수 카운트 (1행은 분류제목이니까)

# 칸 크기 조정
# worksheet.set_column('A:G', 50)
# worksheet.set_row()

while True : 
    # bs4 초기화
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    div_ss_book_box_list = soup.find_all('div', class_='ss_book_box')

    for div_ss_book_box in div_ss_book_box_list :

        # 이미지 (select_one('선택자'))
        img_url = div_ss_book_box.select_one('table div > a img.i_cover')

        # 타이틀, 작가, 가격정보를 모두 포함하는 ul 지목
        ul = div_ss_book_box.select_one('div.ss_book_list > ul')

        # 타이틀
        title = ul.select_one('li > a.bo3')

        # 작가
        author = title.find_parent().find_next_sibling()    # 부모요소의 인접형제요소

        # 작가쪽 영역 데이터 상세 분해
        author_data = author.text.split('|')
        author_name = author_data[0].strip()        # 양쪽공백제거 strip()
        company = author_data[1].strip()
        pub_day = author_data[2].strip()

        # 가격
        price = author.find_next_sibling()
        price_data = price.text.split(', ')[0]

        # 상세페이지 링크
        # title 변수에 a 태그를 이미 지목해놓은 상태 (a태그 요소 전부를 가지고있음)
        # 그 중 href로 작성된 키를 전달하고 해당 value를 받아 변수에 저장
        page_link = title['href']  # 사전에서 데이터 꺼내는것처럼 하기.         (다른방법 : get('href'))


        try :   # 오류 날까봐 try-except처리
            # 이미지 바이트로 변환하기
            # BytesIO 객체의 매개값으로 아까 준비해놓은 img태그의 src값을 전달
            # BytesIO 객체 생성 모듈 미리 임포트
            img_data = BytesIO(req.urlopen(img_url['src']).read())

            # 엑셀에 이미지 저장
            # worksheet.insert_image('배치할 셀 번호', 이미지 제목, {'image_data' : 바이트로변환한이미지, 기타속성. . .})   마지막인수는 사전타입으로
            worksheet.insert_image(f'A{cnt}', img_url, {'image_data' : img_data, 'x_scale':0.5, 'y_scale':0.5})
                                # A2부터,                                                   크기
        except :
            # 파이썬은 블록구조에 아무것도 쓰지 않으면 에러라서 딱히 작성할 코드가 없을 때 pass를 사용.
            pass

        # 엑셀에 나머지 텍스트 저장
        worksheet.write(f'B{cnt}', title.text)
        worksheet.write(f'C{cnt}', author_name)
        worksheet.write(f'D{cnt}', company)
        worksheet.write(f'E{cnt}', pub_day)
        worksheet.write(f'F{cnt}', price_data)
        worksheet.write(f'G{cnt}', page_link)

        cnt += 1
        rank += 1

    # 한 페이지크롤링 종료 후 다음페이지(탭)로 전환
    cur_page_num += 1
    driver.find_element(By.XPATH, '//*[@id="newbg_body"]/div[3]/ul/li['+ str(cur_page_num) +']/a').click()
    del(soup)
    time.sleep(3)

    if(cur_page_num > target_page_num) : 
        print('크롤링 종료')
        break   # While True break

driver.close()
workbook.close()