from day09.class_lib.airplane import AirPlane

class SuperSonicAirPlane(AirPlane):
    NORMAL = 1      #클래스 상수 (대문자) / var
    SUPERSONIC = 2      #두가지 모드가 있다 -> 일반모드 : 1 / SSonic : 2

    def __init__(self):
        self.fly_mode = SuperSonicAirPlane.NORMAL      #멤버 - 비행모드 (초음속비행)

    def fly(self):
        if self.fly_mode == SuperSonicAirPlane.SUPERSONIC:
            print("비행기가 초음속으로 비행합니다.")
        else:
            super().fly()


