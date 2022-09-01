# 입력함수 (java의 scanner)

'''
* 표준 입력함수 input()
- 함수 괄호 안에 사용자에게 질문할 내용을 문자열 형태로 작성합니다.
- input()과 함께 항상 변수를 선언해서 입력값을 받아주셔야 하며 입력받은 데이터의 타입은 str로 저장됩니다. (input()의 리턴타입이 항상 str)
'''

nick = input('너 별명이 뭐야? : ')
print ('내 별명은 ' + nick + '입니다.')

# price = input('음식의 가격 : ')
# people = input('사람 수 : ')
# print('지불할 가격은 : ', price*people, '원' ) (X. str끼리라서 곱셈이 안된다.)

# 입력값이 만약 정수, 실수라면 input 함수 자체를 int(), float()함수로 감싸주시면 됩니다.
# input 함수의 리턴값이 문자열이라고 했으니까, 변환해서 대입하면 끝.
price = int(input('음식의 가격 : '))
people = int(input('사람 수 : '))
print('지불할 가격은 : ', price*people, '원' )
# 왜 안되지 ...??;;