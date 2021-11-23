#딕셔너리의 추가, 변경, 삭제, 조회

d = {'태훈':13, '하은':9}
print(d)

#요소 추가
d['송희'] =10
print(d)

#요소 변경 - 하은이 나이를 14로 변경
d['하은'] = 14
print(d)

#모든 값 가져올때
print(d.values())

#키와 값 모두 가져올때
print(d.items())

#for문으로 조회
for x, y in d.items():
    print(x, y)

#요소 삭제 - pop(키이름)
print(d.pop('태훈'))
print(d)
