#단위 변환 클래스
#inch를 mm로 변환하기
# 1 in = 25mm

class ScaleConverter:
    def __init__(self, units_from, units_to, factor):
        self.units_from = units_from    # 기준단위
        self.units_to = units_to        # 변환단위
        self.factor = factor            # 변환요소

    def convert (self, value):
        return self.factor * value #변환 값 * 25

if __name__ =="__main__":
    sc = ScaleConverter("inches", "mm", 25)
    print("Converting 2 inches")
    print(str(sc.convert(2)) + sc.units_to)
