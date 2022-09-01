'''
* 리스트 내부 요소 삭제
1. remove() : 삭제할 값을 직접 지정하여 삭제
2. 내장함수 del() : 삭제할 요소의 인덱스를 통해 삭제합니다.
3. clear() : 리스트 내부 요소를 전체삭제
'''

points = [88, 99, 56, 92, 100, 78]
points.remove(92)
print(points)

del(points[2]) # 내장함수라 list말고 다른데에서도 쓸수있다.
print(points)

points.clear()
print(points)



# 문제
pokemon = ['피카츄', '라이츄', '파이리', '꼬부기', '버터풀']

'''
- 삭제할 이름을 입력받아서 그에 해당하는 이름을 실제로 리스트에서 삭제한 후 정보를 출력하세요. (리스트 출력)
- remove()와 del()을 이용하여 각각 출력해보세요.
'''

delmon = input('삭제할 포켓몬 : ')

# remove 버전
#pokemon.remove(delmon)

# del 버전
# range (len(pokemon)) -> range(5) -> range(0,5,1) -> [0,1,2,3,4]
for idx in range(len(pokemon)) :
    if delmon == pokemon[idx] :
        del(pokemon[idx])
        break

print('삭제 후 정보 : ', pokemon)