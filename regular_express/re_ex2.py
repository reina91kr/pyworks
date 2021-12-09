import re

str = "123?45yy7890"
# p = re.compile("[0-9]{3}") #0-9 중 1개나 3개의 수로 이루어진 수를 찾아라

# m = re.findall(p, str)      #MATCH는 하나만 찾기 / FINDALL은 리스트형태로 다 찾아라
m = re.findall("[0-9]{1,3}", str) #compile을 안쓰고 범위를 바로 설정할 수도 있음

print(m)


m2 = re.findall("[A-z]+", str)

print(m2)
