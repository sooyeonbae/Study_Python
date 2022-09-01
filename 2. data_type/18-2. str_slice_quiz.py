# 내 코든데... 년도 붙이는게 안된다 왜지!?
# nm1 = input('주민등록번호 앞자리 : ')
# nm2 = input('주민등록번호 뒷자리 : ')

# yy = int(nm1[:2])
# mm = nm1[2:4]
# dd = nm1[4:]
# gen = nm2[0]

# gender = '여자'
# if gen == '1' or gen == '3' :
#     gender = '남자'

# fullyy = 0
# if gen == '1' or gen == '2' :
#     fullyy = 1900 + yy
# else :
#     fullyy = 2000 + yy

# print(f'{fullyy}년 {mm}월 {dd}일 {2022-fullyy}세 {gender}')



ssn = input('주민등록번호를 입력하세요: ')
#921013-1234567

print('주민등록번호 앞자리:', ssn[:6])
print('주민등록번호 뒷자리:', ssn[7:])

year = int(ssn[:2]) # 이따 계산해야 대니까 (출생년도, 나이)
month = ssn[2:4]
day = ssn[4:6]
gender_num = ssn[7]

gender = '여자'

if gender_num == '1' or gender_num == '3':
    gender = '남자'

birth_year = 0

if gender_num == '1' or gender_num == '2':
    birth_year = 1900 + year
else:
    birth_year = 2000 + year

age = 2022 - birth_year

print(f'{birth_year}년 {month}월 {day}일 {age}세 {gender}')
