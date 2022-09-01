# 자동클릭 반복문

'''
네이버로 접속하셔서 뉴스스탠드 위쪽에 있는 파란색 '뉴스홈' 링크를
클릭하세요.

상단에 있는 메뉴 중 정치, 경제, 사회, 생활/문화, 세계, IT/과학
탭을 돌아다니면서 헤드라인 뉴스 4개씩 클릭해 주시면 됩니다.
뒤로가기는 driver.back() 메서드로 뒤로가기 가능합니다.

XPATH를 따다 보면 규칙을 발견하실 수 있을 겁니다.
반복문 이용해서 클릭 명령을 내려 주시면 됩니다.
24개의 명령을 일일히 쓰라는 게 아니에요. 규칙을 꼭 발견 하세요.
상단의 탭에도 규칙이 존재 하고요
뉴스도, 사진이 있는 뉴스와 그렇지 않은 뉴스가 XPATH가 조금씩 다른 것을 유념하세요.
'''

'''
XPATH (주의!! 클릭해야되는 상황에서 XPATH 따오기)
(상단 탭) /html/body/section/header/div[2]/div/div/div[1]/div/div/ul/li[2]/a/span
        //*[@id="lnb"]/ul/li[3]/a/span
        //*[@id="lnb"]/ul/li[4]/a/span
        . . .
        //*[@id="lnb"]/ul/li[7]/a/span


(기사)   //*[@id="main_content"]/div/div[2]/div[1]/div[1]/div[1]/ul/li[1]/div[2]/a
        //*[@id="main_content"]/div/div[2]/div[1]/div[2]/div[1]/ul/li[1]/div[2]/a
        . . .
        //*[@id="main_content"]/div/div[2]/div[1]/div[4]/div[1]/ul/li[1]/div[2]/a

상단탭2)  //*[@id="main_content"]/div/div[2]/div[1]/div[1]/div[2]/ul/li[1]/div[2]/a         ## 상단탭1과 뒤에서 세번째숫자 다름
        //*[@id="main_content"]/div/div[2]/div[1]/div[2]/div[2]/ul/li[1]/div[2]/a
        . . .
        //*[@id="main_content"]/div/div[2]/div[1]/div[4]/div[2]/ul/li[1]/div[2]/a

상단탭3)  //*[@id="main_content"]/div/div[2]/div[1]/div[1]/div[2]/ul/li[1]/div[2]/a         ## 상단탭2와 동일
        //*[@id="main_content"]/div/div[2]/div[1]/div[2]/div[2]/ul/li[1]/div[2]/a
        . . .
        //*[@id="main_content"]/div/div[2]/div[1]/div[4]/div[2]/ul/li[1]/div[2]/a


        //*[@id="main_content"]/div/div[2]/div[1]/div[3]/div[2]/ul/li[1]/div[2]/a       ## 사진있는것 3번째
        //*[@id="main_content"]/div/div[2]/div[1]/div[4]/div[2]/ul/li[1]/div/a          ## 4번째지만 사진없음

        //*[@id="main_content"]/div/div[2]/div[1]/div[4]/div[2]/ul/li[1]/div/a          ## 상단탭 다른경우, 4번째지만 사진없음

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome('/Users/baesy/Desktop/web_development/Python/chromedriver')


driver.get('https://www.naver.com')
time.sleep(0.5)

# 뉴스홈으로 이동
driver.find_element(By.XPATH, '//*[@id="NM_NEWSSTAND_HEADER"]/div[2]/a[1]').click()
time.sleep(0.5)

# 상단탭 1로 이동(정치)
driver.find_element(By.XPATH, '/html/body/section/header/div[2]/div/div/div[1]/div/div/ul/li[2]/a/span').click()
time.sleep(0.5)

# 상단탭 [1]의 기사 4개 반복문
for n in range(1, 5) :
    try :
        driver.find_element(By.XPATH, '//*[@id="main_content"]/div/div[2]/div[1]/div['+ str(n) +']/div[1]/ul/li[1]/div[2]/a').click()
    except :
        driver.find_element(By.XPATH, '//*[@id="main_content"]/div/div[2]/div[1]/div['+ str(n) +']/div[1]/ul/li[1]/div/a').click()
    time.sleep(0.5)
    driver.back()
    time.sleep(0.5)

    # 상단탭 (경제~세계) 반복문    
for n in range(3, 8) :
    driver.find_element(By.XPATH, '//*[@id="lnb"]/ul/li['+ str(n) +']/a/span').click()
    time.sleep(0.5)
    # 상단탭 안 기사 4개 반복문
    for n in range(1, 5) :
        try :
            driver.find_element(By.XPATH, '//*[@id="main_content"]/div/div[2]/div[1]/div['+ str(n) +']/div[2]/ul/li[1]/div[2]/a').click()
        # 사진없는기사라서 XPATH 오류난경우
        except :
            driver.find_element(By.XPATH, '//*[@id="main_content"]/div/div[2]/div[1]/div['+ str(n) +']/div[2]/ul/li[1]/div/a').click()
        time.sleep(0.5)
        driver.back()
        time.sleep(0.5)

