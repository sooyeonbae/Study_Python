'''
* 참조변수 (reference variable)
- 객체를 참조하는 주소값을 담고있는 변수
'''

a = 3
b = a
print(a,b) # : 3 3

a = 5
print(a,b) # : 5 3

list1 = [1,2,3]
list2 = list1
print('list1 : ', list1)    # : [1, 2, 3]
print('list2 : ', list2)    # : [1, 2, 3]

# 리스트는 객체라 list1과 list2의 주소값이 공유된다.
list1[0] = 6
list2[1] = 9
print('list1 : ', list1)    # : [6, 9, 3]
print('list2 : ', list2)    # : [6, 9, 3]
# 주소값 (둘이 주소값 같다.)
print('list1의 주소값 : ', id(list1))
print('list2의 주소값 : ', id(list2))



# 다른 객체 쓰는법(주소값 공유 안하게하는법) - 리스트를 먼저 선언하고, 리스트 내부 요소들을 .copy()를 이용해 복사하여 전달
list1 = [1,2,3]
list2 = []
list2 = list1.copy()
list1[0] = 6
list2[1] = 9
print('list1 : ', list1)    # : [6, 2, 3]
print('list2 : ', list2)    # : [1, 9, 3]
# 주소값 (둘이 주소값 다르다.)
print('list1의 주소값 : ', id(list1))
print('list2의 주소값 : ', id(list2))