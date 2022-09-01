# 셀레늄 : 웹 자동화 및 웹의 소스코드를 수집하는 모듈

# cmd -> pip install selenium(셀레늄 라이브러리 다운로드)
# (나는 터미널 가서 pip3 install selenium)

# 셀레늄 임포트 (그 중에서도 webdriver) (문법 바껴서 임포트 두개해줘야함...)
from selenium import webdriver
from selenium.webdriver.common.by import By

# 웹드라이버 정상적으로 동작시키기위해 브라우저에 웹드라이버 프로그램 설치 
# (크롬 : https://chromedriver.chromium.org/downloads) 
# 버전에 맞게 다운로드(나는 버전 103.0.5060.53라서 크롬드라이버도 같은버전, 
# chromedriver_mac64_m1.zip 으로 받음.
#  -> 파이썬 폴더 안에 풀어놨다.)

# 다운로드 받은 크롬 물리드라이버 가동 명령. (변수에 받아주기)
driver = webdriver.Chrome('/Users/baesy/Desktop/web_development/Python/chromedriver')

# 물리드라이버로 사이트 이동 명령
driver.get('https://www.naver.com')

# 로딩시간끌어주기
import time
time.sleep(1.5)

'''
# 네이버 로그인하기
# 로그인영역 지목해서 클릭하게하기 - F12개발자도구 - 지목할곳 클릭해서 elements 태그 가서 해당영역 우클릭 - copy XPath
# 자동으로 버튼이나 링크 클릭 제어하기
# 요소를 지목하기위한 변수 선언해주고 xpath 알려주기
# xPath : XML Path Language (문서의 특정 요소나 속성에 접근하기 위한 경로를 지정하는 언어.
#                              지목하기 좋아서 이거 쓴다. 요소를 중복없이 정확하게 표현하기 쉬운 언어.)

# 옛날문법 ) login_btn = driver.find_element_by_xpath('//*[@id="account"]/a')
login_btn = driver.find_element(By.XPATH, '//*[@id="account"]/a')

# 클릭 명령
login_btn.click()

time.sleep(1) # 로그인화면 띄운뒤 1초 대기

# 로그인창 xPath 따와서 자동으로 텍스트 입력시키기
id_input = driver.find_element(By.XPATH, '//*[@id="id"]')
id_input.send_keys('bb7bb3bb1')
time.sleep(1)
pw_input = driver.find_element(By.XPATH, '//*[@id="pw"]')
pw_input.send_keys('asdfasdf') 
time.sleep(1)

# 로그인 버튼 누르기 (변수선언없이)
driver.find_element(By.XPATH, '//*[@id="log.login"]').click()
# 네이버 서버가 감지하고 막아놨다. (뚫는 방법 있지만 알아서 찾아봐라 - '셀레늄 네이버 로그인' 검색)
'''


# QUIZ )
# 네이버에 접속하셔서 검색창에 '오늘 날씨'를 입력하셔서
# 검색 후 가장 첫번째로 뜨는 네이버 뉴스를 띄워주세요.

driver.find_element(By.XPATH, '//*[@id="query"]').send_keys('오늘 날씨')
driver.find_element(By.XPATH, '//*[@id="search_btn"]').click()

time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="sp_nws_all1"]/div[1]/div/a').click()