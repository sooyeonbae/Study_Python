'''
* 문자열 관리 함수, 메서드

+) 함수와 메서드 차이점
함수 : 모듈(.py 파일들)내부에서 공용적으로 사용할 수 있는 기능의 집합. 단독 호출 가능
메서드 : 클래스에 소속된 함수, 특정 자료형(문자열, 정수형 등) 전용함수

'''

# 내장 함수 len() : 순차형 자료(sequence)의 내부 데이터 개수를 구함.
# len()은 함수라서 문자열 전용이 아니고 다른 자료형에서도 사용 가능하다.

s = 'python programming'

count = 0
for c in s :
    count += 1
print('s의 글자 수 : ', count)

print('s의 글자 수 : ', len(s))



# 문자열 메서드 find(), rfind() : 문자열 내부에 특정 문자를 검색하여 해당 문자의 인덱스 번호를 알려줍니다.
# find() : 앞에서부터, rfind() : 뒤에서부터 탐색
# 메서드라서 String에서만 사용 가능하다. 문자열 전용함수. 타겟이 필요하다.  타겟.find()

print(s.find('o'))
print(s.rfind('o'))

print(s.find('program'))    # 단어도 가능. 단어의 시작인덱스 리턴

print(s.find('없는거찾아보기')) # 탐색시 문자를 발견하지 못하면 -1 리턴


# 메서드 count() : 문자열 내부에 찾는 단어의 출현횟수 반환
msg = """
    내가 그린 기린 그림은 목이 긴 기린 그림이고
    네가 그린 기린 그림은 목이 안긴 기린 그림이다.
"""
print('"기린" 단어의 출현 횟수 : ', msg.count('기린'))


# in    /   not in
# 특정 문자가 있는 인덱스나 번호 및 횟수는 관심 없고, 단순히 포함여부나 빠르게 확인하고 싶다면 in 키워드를 사용합니다.
# 결과 값은 True, False
print('a' in s) # : True
print('q' in s) # : False
print('z' not in s) # : True
print('pro' in s) # : True



'''
- 사용자에게 데이터를 입력받을 때 등등 입력값의 형태를 검사하는 메서드
1. isdecimal() : 모든 문자가 숫자 형태인지를 검사.
2. isalpha() : 모든 문자가 영문 알파벳인지를 검사.
3. islower() : 모든 문자가 영문 소문자인지를 검사.
4. isupper() : 모든 문자가 영문 대문자인지를 검사.
'''

print('15 + 8 = ???')
while True : 
    answer = (input(': '))   # int로 입력받으면 숫자 이외의 문자를 입력하면 오류난다.
                               
    if answer.isdecimal() :  # 입력값이 정수인지 먼저 확인 필요
        answer = int(answer)
    else :
        print('정답은 숫자로만 입력해주세요.')
        continue
    
    if answer == 23 :
        print('정답입니다.')
        break
    else :
        print('틀렸습니다.')
    