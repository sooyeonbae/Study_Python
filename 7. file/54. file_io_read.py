# 파일 읽기 (실행시키면 오류나는데 왜 오류나는지 모르겠다... 코드멀쩡한데 ㅜ)

'''
* 파일 읽기 기능 (read)
- 파일로부터 데이터를 읽어들일 때에는 분량에 따라 적당한 메서드를 선택해서 사용합니다.

1. read() : 파일 전체를 통째로 읽어서 리턴
2. readline() : 파일 데이터를 한 줄씩 읽어서 리턴
3. readlines() : 파일 전체를 읽어서 한 줄씩 분리한 후에 리스트에 담아서 리턴
'''

file_path = '/Users/baesy/Desktop/web_development/Python/test/test3.txt'

# try :
#     f = open(file_path, 'r')
#     text = f.read()
#     print(text)
# except :
#     print('파일 로드 실패')
# finally :
#     f.close()


# readline() 메서드는 자동으로 \n을 기준으로 하여
# 데이터를 줄 단위로 읽어들이기 때문에
# 메모리 부담을 좀 더 줄일 수 있습니다.

# try :
#     f = open(file_path, 'r')
#     text = f.readline()
#     print(text)
# except :
#     print('파일 로드 실패')
# finally :
#     f.close()


# try :
#     f = open(file_path, 'r')
#     while True :
#         text = f.readline()
#         print(text)
#         if len(text) == 0 : # 더 읽어들일 데이터가 없다면
#             break
# except :
#     print('파일 로드 실패')
# finally :
#     f.close()



# readlines() 는 파일 데이터를 한 줄씩 읽어서
# 리스트에 담아서 리턴하기 때문에
# 읽은 데이터를 리스트 문법을 사용해서 처리할 수 있습니다.

try :
    f = open(file_path, 'r')
    text = f.readlines()
    print(text)
    
    text.reverse() # 역순배치

    for t in text : # readline처럼 한 행씩 출력
        print(t)    
except :
    print('파일 로드 실패')
finally :
    f.close()