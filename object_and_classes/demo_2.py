class Vehicle:
    def __init__(self, started=False, speed=0):
        self.started = started
        self.speed = speed

    def start(self):
        self.started = True
        print("Car started, let's ride!")

    def stop(self):
        self.speed = 0

    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print('Vroooom!')
        else:
            print("You need to start the car first")


class Car(Vehicle):
    trunk_open = False

    def open_trunk(self):
        self.trunk_open = True

    def close_trunk(self):
        self.trunk_open = False


class Motorcycle(Vehicle):
    def __init__(self, center_stand_out = False):
        self.center_stand_out = center_stand_out
        super().__init__()

car = Vehicle()
car1 = Car()
motor = Motorcycle()
# print(car1.close_trunk())
# print(car.start())
# print(car.increase_speed(40))
# print(car.speed)
print(motor.start())
print(motor.increase_speed(40))
print(motor.speed)