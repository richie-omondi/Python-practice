class Car():
    color = ''
    model = ''
    speed = 0
    brand = ''
    fuel_tank = 0
    number_of_wheels = 0
    engine_size = 0
    mileage = 0
    year = 2017

    def current_speed(self):
        speed = 100
        print(f"Current speed is {self.speed}")

    def navigation(self, second_direction, direction = "Right", ):
        print(f"Turn {direction} and turn {second_direction}")

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car = Car("Lamborghini", "Urus")
car.engine_size = 396
car.number_of_wheels = 4
car.mileage = 0
car.speed = 305
car.color = "Yellow"

print(f"Richard's car brand: {car.brand}")
print(f"Richard's car model: {car.model}")
car.current_speed()
car.navigation(second_direction="Left", direction="Right")



