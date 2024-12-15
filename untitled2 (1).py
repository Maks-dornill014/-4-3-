class Transport:
    def __init__(self, speed):
        
        self.speed = speed

    def move(self, distance):
        
        if self.speed <= 0:
            raise ValueError("Швидкість повинна бути більше нуля.")
        return distance / self.speed


# Підклас Автомобіль
class Car(Transport):
    def __init__(self, speed, brand):
        
        super().__init__(speed)
        self.brand = brand

    def __str__(self):
        return f"Автомобіль марки {self.brand}, швидкість: {self.speed} км/год."



class Bicycle(Transport):
    def __init__(self, speed, type_bike):
        
        super().__init__(speed)
        self.type_bike = type_bike

    def __str__(self):
        return f"{self.type_bike.capitalize()} велосипед, швидкість: {self.speed} км/год."



class Airplane(Transport):
    def __init__(self, speed, airline):
       
        super().__init__(speed)
        self.airline = airline

    def __str__(self):
        return f"Літак авіакомпанії {self.airline}, швидкість: {self.speed} км/год."



car = Car(120, "Toyota")
print(car)
print(f"Час на поїздку 240 км: {car.move(240):.2f} год.")

bike = Bicycle(20, "гірський")
print(bike)
print(f"Час на поїздку 50 км: {bike.move(50):.2f} год.")

airplane = Airplane(900, "SkyAir")
print(airplane)
print(f"Час на переліт 1800 км: {airplane.move(1800):.2f} год.")
