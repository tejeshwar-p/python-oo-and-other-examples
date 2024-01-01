class Motorcycle:
    def __init__(self, gear, speed):
        self.gear = gear
        self.speed = speed

    def __repr__(self):
        return repr((self.gear, self.speed))


yamaha_r_15 = Motorcycle(5, 200)
bajaj_pulsar_150 = Motorcycle(5, 120)

print(yamaha_r_15)
print(bajaj_pulsar_150)
