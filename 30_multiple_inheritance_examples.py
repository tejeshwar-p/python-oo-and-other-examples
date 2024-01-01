class LandAnimal:
    def walk(self):
        print("Walk")


class WaterAnimal:
    def swim(self):
        print("Swim")


class Amphibian(LandAnimal, WaterAnimal):
    pass


frog = Amphibian()
frog.walk()
frog.swim()


