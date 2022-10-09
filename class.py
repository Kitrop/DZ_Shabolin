class Car():
    def __init__(self, speed, power, health):
        self.speed = speed
        self.power = power
        self.health = health

    def about(self):
        return self.speed



Car1 = Car(1, 2, 3)
Car2 = Car(10, 2, 3)

print( Car1.about() > Car2.about() )