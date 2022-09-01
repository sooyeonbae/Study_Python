'''
* 사용자의 입력을 파일(xxx.txt)에 저장하는 프로그램을 작성하세요.
(단, 프로그램을 다시 실행하더라도 파일명이 동일하다면
기존 작성한 내용을 그대로 유지하고
새로 입력된 내용이 추가되어야 합니다.
파일명도 마지막에 입력받아서 생성하세요.)
'''

text = ''

print("저장할 내용을 입력 ('그만'이라고 입력시 종료됩니다.)")
while True :
    text_input = input('> ')
    text += text_input + '\n'
    
    if text_input == '그만' :
        file_name = input('파일명을 입력 : ')
        break

file_path = r'/Users/baesy/Desktop/web_development/Python/test/'+ file_name +'.txt'

try :
    f = open(file_path, 'a')
    f.write(text)
    print('파일 저장 성공!')

except :
    print('파일 저장 실패')

finally :
    f.close()