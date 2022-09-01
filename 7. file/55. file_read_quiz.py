'''
* points.txt 파일의 숫자값을 모두 읽어서
총합과 평균을 구한 뒤
총점, 평균값을 result.txt라는 파일에
쓰는 프로그램을 작성해 보세요.
'''

'''
파이썬의 에러확인하기 (java의 printStackTrace)
1. traceback 모듈을 import한다.
2. except 부분에
    print(traceback.format_exc())
'''

import traceback


# file_path = '/Users/baesy/Desktop/web_development/Python/test/points.txt'
    

try :
    f = open('/Users/baesy/Desktop/web_development/Python/test/points.txt', 'r')
    numlist = f.read().split()
except :
    print('파일 로드 실패')
    print(traceback.format_exc())
finally :
    f.close()
    


sum = 0
for n in numlist :
    score = int(n)
    sum += score

avg = sum / len(numlist)


try :
    f = open('/Users/baesy/Desktop/web_development/Python/test/result.txt', 'w')
    data = f'총점 : {sum}점, 평균 : {avg:0.2f}점'
    f.write(data)
    print('파일 저장 성공')
except :
    print('파일 저장 실패')
finally :
    f.close()

