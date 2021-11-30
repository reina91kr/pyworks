#Converter 클래스 정의
#온도 변환기 : 화씨온도 (F) = 섭씨온도(C) * 1.8 + 32

from day09.class_lib.scaleconverter import ScaleConverter

class Converter(ScaleConverter):
    def __init__(self, units_from, units_to, factor, offset): # C,F, 1.8, 32
        super().__init__(units_from, units_to, factor)
        self.offset = offset

    def convert(self, value):
        return self.factor * value + self.offset

conv = Converter('C', 'F', 1.8, 32)
print("Converting 20C")
print(str(conv.convert(20)) + conv.units_to)

print("%.2f F" % conv.convert(21))

