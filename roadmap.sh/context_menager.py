from contextlib import contextmanager

class Open_File():
    def __init__(self , filename , mode):
        self.filename = filename
        self.mode = mode
    def __enter__(self):
        self.file = open(self.filename , self.mode)
        print('opened')
        return self.file
    def __exit__(self , exc_type , exc_val , traceback):
        self.file.close()
        print("closed")

with Open_File('s1mple.txt','w') as f:
    f.write('testing')

print(f.closed)

# той самий спосіб тільки через імпорт [contextmanager]
@contextmanager
def opinFile(file, mode):
    # відкриваємо файл
    f = open(file, mode)
    print('opened')
    # пауза — передаємо файл в "as f"
    # тут виконується блок with
    yield f
    # після блоку with — закриваємо файл
    f.close()
    print('closed')

# відкриваємо файл 's1mple.txt' в режимі запису
with opinFile('s1mple.txt', 'w') as f:
    f.write('abrakadabra')  # записуємо текст

# перевіряємо чи файл закритий (True = закритий)
print(f.closed)
# через yield
@contextmanager
def op1nFile(file, mode):
    f = open(file, mode)
    print('opened')
    try:
        yield f
    finally:
        f.close()   # закриється навіть якщо виникне помилка
        print('closed')
        print(f.closed)
    
with op1nFile('s1mple.txt', 'w') as f:
    f.write('abrakadabraaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')  # записуємо текст
