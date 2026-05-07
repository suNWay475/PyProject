class Product:
    def __init__(self , name , price ):
        self.name = name
        self.price = price
    def info(self):
        return f"Назва:{self.name}, Ціна:{self.price}" 
    
class Food(Product):
    def __init__(self, name, price, expiry_date):
        super().__init__(name, price) 
        self.expiry_date = expiry_date  

    def check_expiry(self):
        print(f"Термін придатності: {self.expiry_date}")


class Electronics(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)   
        self.warranty = warranty  

    def check_warranty(self):
        print(f"Гарантія: {self.warranty}")

food1 = Food("Молоко" , '35 гривень' , '2026-05-10')
electronics1 = Electronics("Телефон", '15.000 гривень' , '2 роки')
    
print(food1.info())
food1.check_expiry()

print(electronics1.info())
electronics1.check_warranty()