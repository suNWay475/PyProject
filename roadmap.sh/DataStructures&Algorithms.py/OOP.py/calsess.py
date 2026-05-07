#    Найпоширеніші dunder методи
# Метод                   Коли викликається
# __init__                  при створенні об'єкта
# __str__                   при print()
# __len__                   при len()
# __add__                   при +
# __repr__                  при виводі в консолі




#1
class Car:
    def __init__(self , brand):
        self.brand = brand
        self.speed = 0

    def drive(self):
        print("driving")

    def accelerate(self):
        self.speed += 10
        print(f'Speed:{self.speed}')

car1 = Car("toyota")

def tostopsign(car):
    while True:
        car.accelerate()
        if car.speed >= 90 :
            break
        else:
            car.accelerate()


tostopsign(car1)
#2
class Сlient:
    def __init__(self , name):
        self.name = name
        self.haveorders = 0
    
    def __str__(self):
        return f"Замовлень: {self.haveorders}, Ім'я {self.name} "

    def __len__(self):
        return self.haveorders

    def countorders(self):
        self.haveorders += 1
        print(f'Замовлень:{self.haveorders}')

def neworder(client):
    print("Додано нове замовлення, Кількість ", end="")
    client.countorders()



client1 = Сlient("Alex")


neworder(client1)
print(client1)

