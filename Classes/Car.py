class Car:
    brand = None
    model = None

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # def print(self):
    #     print(self.brand, self.model)
    def fullName(self):
        return f"{self.brand}{self.model}"


class Electric(Car):
    battery_size = None

    def __init__(self, battery_size, brand, model):
        super().__init__(brand, model)
        self.battery_size = battery_size




elaectric_car = Electric("85kwh", "Tesla", "S")
print(elaectric_car.fullName())
