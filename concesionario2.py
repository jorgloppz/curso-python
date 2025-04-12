class Car:
    def __init__(self, model, price):
        self.model = model 
        self.price = price 
        self.available = True

    def sell(self):
        if self.available:
            self.available = False 
            print(f"El carro {self.model} ha sido vendido")
        else:
            print(f"El carro {self.model} ya no está disponible")

    def __repr__(self):
        return f"{self.model} (${self.price})"


class Person:
    def __init__(self, name, id):
        self.name = name 
        self.id = id
        self.bought_cars = []

    def buy_car(self, car):
        if car.available:
            car.sell()  # Marca el carro como vendido
            self.bought_cars.append(car)
            print(f"{self.name} ha comprado el vehículo {car.model} por {car.price}")
        else:
            print(f"El carro {car.model} ya no está disponible")

    def sell_car(self, car, dealer):
        if car in self.bought_cars:
            self.bought_cars.remove(car)
            dealer.add_car(car)  # Añade el carro al inventario del concesionario
            print(f"Tu carro {car.model} lo pondremos a la venta y te avisaremos cuando completemos el proceso")
        else:
            print(f"No tienes el carro {car.model} en tu colección")


class Dealer:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        if car not in self.cars:
            self.cars.append(car)
            print(f"El carro {car.model} ha sido incluido en nuestra línea de carros para la venta")
        else:
            print(f"El carro {car.model} ya está en la línea de carros para la venta")

    def sell_car(self, car):
        if car in self.cars:
            if car.available:
                car.sell()
                self.cars.remove(car)
                print(f"El carro {car.model} ha sido vendido")
            else:
                print(f"El carro {car.model} ya no está disponible")
        else:
            print(f"El carro {car.model} no está en la línea de carros para la venta")

    def available_cars(self):
        print("Vehículos disponibles:")
        for car in self.cars:
            if car.available:
                print(f"{car}")


# Crear carros
car1 = Car("spark gt", "20.000.000")
car2 = Car("aveo", "18.000.000")
car3 = Car("toyota hilux", "80.000.000")
car4 = Car("hyundai", "17.000.000")

# Crear personas
person1 = Person("Laura", "0001")
person2 = Person("Andres", "0002")
person3 = Person("Sore", "0003")
person4 = Person("Jorge", "0004")

# Crear dealer
dealer = Dealer()
dealer.add_car(car1)
dealer.add_car(car2)
dealer.add_car(car3)
dealer.add_car(car4)

# Mostrar carros disponibles
dealer.available_cars()

# Comprar un carro
person1.buy_car(car1)

# Mostrar carros disponibles después de la compra
dealer.available_cars()

# Vender un carro de una persona al dealer
person1.sell_car(car1, dealer)

# Mostrar carros disponibles después de añadir un carro al dealer
dealer.available_cars()

# Vender un carro que no está en la lista de comprados
person4.sell_car(car4, dealer)

#Mostrar carros disponibles después de la compra
dealer.available_cars()


