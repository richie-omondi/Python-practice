class Car():
    brand = ''
    model = ''
    year = 0
    speed = 0
    mileage = 0

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

class ElectricCar(Car):
    battery_capacity = 0
    def __init__(self, brand: str, model: str, year: int, battery_capacity: int):
        super().__init__(brand, model, year)

class CEngineCar(Car):
    engine_capacity = 0

car = Car("Tesla", "Model S", 2022)

electric_car = ElectricCar("Tesla", "Model Y", 2020, 2000)

c_engine_car = CEngineCar("Toyota", "Corola S", 2020)

print(f"CEngine car brand: {c_engine_car.brand}")

class Toyota(CEngineCar):
    new_variable = 0

new_class = Toyota()
new_class.engine_capacity = 0

