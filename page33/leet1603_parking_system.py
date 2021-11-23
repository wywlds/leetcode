class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.counts = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.counts[carType -1] > 0:
            self.counts[carType - 1] -= 1
            return True
        else:
            return False