class Car:
    def __init__(self, color, length, company):
        self.color = color
        self.length = length
        self.company = company

    def __str__(self):
        return f"{self.color} , {self.length} , {self.company}"

    def print(self):
        print(f"{self.color} , {self.length} , {self.company}")


car1 = Car("m", "4", "c")

car1.print()
