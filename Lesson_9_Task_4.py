class Car():
    is_police = False

    def __init__(self, color, name):
        self.color = color
        self.name = name
        print(f"Man, we got a new car! Our {self.name} lookin' very nice with {self.color.casefold()} color!")

    def go(self, speed):
        self.speed = speed
        print(f"We drivin'! Speed: {self.speed}")

    def stop(self):
        self.speed = 0
        print(f"We stopped drivin'...")

    def turn(self, direction):
        if direction == 'left' or direction == 'right':
            print(f"We turned {direction}!")
        else:
            print(f'There is no {direction} turn, my dude!')

    def show_speed(self):
        print(f'Our speed is {self.speed}!')


class TownCar(Car):
    def go(self, speed):
        self.speed = speed
        print(f"We drivin'! Speed: {self.speed}")
        if self.speed > 60:
            print("You drivin' too fast my man!")
    def show_speed(self):
        print(f'Our speed is {self.speed}!')
        if self.speed > 60:
            print("You drivin' too fast my man!")


class SportsCar(Car):
    pass


class WorkCar(Car):
    def go(self, speed):
        self.speed = speed
        print(f"We drivin'! Speed: {self.speed}")
        if self.speed > 40:
            print("You drivin' too fast my man!")
    def show_speed(self):
        print(f'Our speed is {self.speed}!')
        if self.speed > 40:
            print("You drivin' too fast my man!")


class PoliceCar(Car):
    is_police = True

subaru = SportsCar('Blue', 'Subaru')
subaru.go(90)
subaru.turn('left')
subaru.go(110)
subaru.stop()
print('Are we cops? ' + str(subaru.is_police))

kamaz = WorkCar('Red', 'KAMAZ')
print('Are we cops? ' + str(kamaz.is_police))
kamaz.go(40)
kamaz.go(45)
kamaz.turn('right')
kamaz.stop()
kamaz.show_speed()

mercedes = PoliceCar('Black', 'Mercedes')
print('Are we cops? ' + str(mercedes.is_police))
mercedes.go(100)
mercedes.stop()

kia = TownCar('Grey', 'KIA')
print('Are we cops? ' + str(kia.is_police))
kia.go(69)
kia.turn('out of bounds')
kia.show_speed()
kia.stop()