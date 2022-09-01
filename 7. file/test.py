text = input('내용 입력 : ')
file_name = input('파일명 : ')

file_path = r'/Users/baesy/Desktop/web_development/Python/test/'+ file_name +'.txt'

try :
    f = open(file_path, 'a')
    f.write(text)
    print('파일 저장 성공!')

except :
    print('파일 저장 실패')

finally :
    f.close()