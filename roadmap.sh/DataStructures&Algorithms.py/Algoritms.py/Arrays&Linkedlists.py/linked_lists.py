# Linked_lists


class Car:

    wheels = 4 

    def __init__(self , brand , color ):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"name: {self.brand} is driving")

car1 = Car('Toyota', "red")
car2 = Car('BMW', "black")

print(car1.brand)
print(car2.color)
car1.drive()

print(Car.wheels)

# linked 2
class Node:
    def __init__(self, value):
        self.value = value   
        self.next = None     


node1 = Node(10)   # → value=10, next=None
node2 = Node(20)   # → value=20, next=None

node1.next = node2 
# linked 3

