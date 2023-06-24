from tires.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        total = 0
        for tire in self.tire_wear:
            total += tire
        if total < 3.0:
            return False
        else:
            return True 