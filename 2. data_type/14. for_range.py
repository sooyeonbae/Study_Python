'''
* 내장함수 range()
- 순차적으로 증가하는 정수의 순차적 자료형을 만들 때
대괄호 안에 데이터들을 일일이 나열하는 것은 한계가 있기 떄문에,
range()함수를 통해 보다 쉽게 순차형 반복 범위를 지정할 수 있습니다.

ex)
range(begin, end, step)
- begin은 값이 포함되지만(>=) , end는 값이 포함되지 않습니다(<). 
'''

list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1)

list2 = list(range(1,11,1)) # '미만'이라서 11
print(list2)

# step값을 주지 않으면 자동으로 1로 처리 (=jstl의 c:forEach문)
list3 = list(range(4,15))
print(list3)

# range 함수 괄호 안에 값을 한 개만 주면 end로 처리하고
# begin은 0, step은 1로 자동으로 처리.
list4 = list(range(5)) # =  range(0, 5, 1)
print(list4)



# 1부터 100까지의 누적합을 구하는 로직
total = 0
for n in range(1, 101) : #list안쓰고 바로 range 써도 된다.
    total += n
print('1~100까지의 누적합 : ', total)


'''
- 정수를 하나 입력받아서 1부터 해당 수까지의
 모든 소수를 가로로 출력하고, 그 소수의 개수를
 출력하시면 됩니다. (중첩 for문)

 ex) 입력값: 12 
    소수: 2, 3, 5, 7, 11
    개수: 5개
'''
inputnum = int(input('정수를 입력하세요 : '))
i = 0 # 소수가 몇개인지
for n in range(1, inputnum+1) :
    cnt = 0 # 소수 판별을 위해 나누어 떨어진 횟수를 체크할 변수.
    for m in range (1, n+1) :
        if n % i == 0 :
            cnt += 1
    # 소수판별이 끝나고나서
    if cnt == 2 :
        m += 1
        print (n, end = '')
print( ' \n 소수들의 개수 : ' + i + '개')