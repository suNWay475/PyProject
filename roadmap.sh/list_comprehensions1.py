# звичайний спосіб , дуже довго
numbers = [ 1 , 2 , 3 , 4 , 5 , 6]
squares = []
for n in numbers:
    squares.append(n ** 2)
print(squares)
# те саме тільки займе меньше місця і легше
numbers = [ 1 , 2 , 3 , 4 , 5 , 6]
squares = [n ** 2 for n in numbers]

# ще один приклад 
words = ['hello','world','try','one','more']
squares = [w.upper() for w in words]
print(squares)

lenght = [len(w) for w in words]
print(lenght)

# з умовою , звичайний спосіб
numbers = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8]
evens = []
for n  in numbers:
    if n % 2 == 0:
        evens.append(n)
print(evens)

# з умовою з Lists Comprehensions
numbers = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8]
evens = [n for n in numbers if n % 2 == 0]
print(evens)
# ще один приклад 
numbers = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20]
bigger = [n for n in numbers if n >= 10 ]
print(bigger)