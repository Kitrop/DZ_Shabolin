class Car():
    def __init__(self, brand, maxSpeed, color):
        self.brand = brand
        self.maxSpeed = maxSpeed
        self.color = color

    def about(self):
        print("У " + self.brand + " максимальная скорость:" + self.maxSpeed + ", самый популярный цвет у данной марки авто:" + self.color)



Car1 = Car("Lamborgini", "500", "Красный")
Car2 = Car("Lada", "150", "Серебристый")