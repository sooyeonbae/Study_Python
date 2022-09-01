
# 리스트를 이용한 간단한 연락처 관리 프로그램

# namelist에 이름, phonelist에 전화번호를 저장해서
# 이름과 전화번호 리스트의 인덱스가 동일하게 증가할 수 있도록 조작.
from __future__ import print_function


namelist = []
phonelist = []

while True:
    print('\n---------- 연락처 관리 프로그램 ----------')
    print('1. 연락처 등록')
    print('2. 연락처 검색')
    print('3. 연락처 삭제')
    print('4. 모든 연락처 조회')
    print('5. 프로그램 종료')
    print('---------------------------------------')

    menu = int(input('메뉴를 입력하세요: '))

    if menu == 1:
        # 파이썬의 블록구조는 비워져 있으면 에러가 발생합니다.
        # 비워놓으려면 pass 키워드를 넣어서 통과시키라고 얘기하면 됩니다.

        # 입력받은 이름과 전화번호 데이터를 각각의 리스트에 추가하세요.
        # 추가 완료 시 "XXX님 연락처 저장 완료!" 를 출력하세요.

        name = input('이름을 입력하세요 : ')
        phone = input('전화번호를 입력하세요 : ')
        namelist.append(name)
        phonelist.append(phone)
        print(f'{name}님의 연락처가 저장되었습니다.')

    elif menu == 2:
        # 입력한 이름이 리스트 내부에서 발견된다면 해당 이름을 통해
        # 인덱스 번호를 추출하여 인덱스를 통해 리스트의 전화번호를 얻어옵니다.
        # 출력예시: "홍길동의 전화번호는 010-1234-5678입니다."
        name = input('검색하려는 회원의 이름 : ')
        
        if name in namelist :
            phone = phonelist[namelist.index(name)]
            print(f'{name}님의 전화번호는 {phone}입니다.')
        else :
            print('없는 회원입니다.')
        
    elif menu == 3:
        # 이름을 입력받아서 해당 이름과 전화번호를 동시에 삭제해 주세요.
        # 이름이 없다면 없다고도 얘기 해 주세요.
        name = input('삭제하려는 회원의 이름 : ')
        if name not in namelist :
            print('없는 회원입니다.')
        else : 
            del(phonelist[namelist.index(name)])
            namelist.remove(name)
            print(f'{name}님의 정보가 삭제되었습니다.')


    elif menu == 4:
        # for문을 통해 리스트 내부의 모든 인덱스에 접근하여 모든 이름과
        # 연락처 정보를 출력하는 코드를 작성합니다.
        # 홍길동 : 010-1234-5678
        # 김철수 : 010-5678-1234...

        for idx in range(len(namelist)) :
            print(f'{namelist[idx]} : {phonelist[idx]}')
        
    elif menu == 5:
        print('프로그램을 종료합니다.')
        break # while True break
    else:
        print('메뉴를 다시 입력해 주세요.')