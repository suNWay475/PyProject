# . будь-який символ, a.c → abc, axc
# \ dцифра (0-9), \d\d → 42
# \ wбуква, цифра, _ ,\w+ → hello
# \ sпробіл, табa, \sb → a b
# + 1 або більше, \d+ → 123
# * 0 або більше, \d* → `` або 123
# ? 0 або 1, colou?r → color, colour
# ^ початок рядка, ^Hello
# $ кінець рядка, world$

import re

phones = [
    "+380-99-123-4567",
    '+380-23-456-9987',  
    '+380-12-456-9087',   
    '099-123-456',   
]
text = '099-123-4567'
result = re.search(r'\+380-\d{2}-\d{3}-\d{4}', text) 

for phone in phones:
    result = re.search(r'\+380-\d{2}-\d{3}-\d{4}', phone) 
    if result:
        print(f'{phone} це правдивий номер')   
    else:
        print("неправильно введиний телефон")


text = 'Привіт 123 world!'

result = re.search(r'\w+ - \d{3} -\w+', text)

