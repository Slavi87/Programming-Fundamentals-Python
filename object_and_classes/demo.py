class Car:
    def __init__(self, started=False, speed=0):
        self.started = started
        self.speed = speed


    def start(self):
        self.started = True
        print("Car started, let's ride!")

    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print('Vroooom!')
        else:
            print("You need to start the car first")

    def stop(self):
        self.speed = 0
        print('Halting')


car1 = Car()
car2 = Car(True)
car3 = Car(True, 50)
car4 = Car(started=True, speed=40)
print(car1.speed)
print(car2.speed)
print(car3.speed)
print(car4.speed)
