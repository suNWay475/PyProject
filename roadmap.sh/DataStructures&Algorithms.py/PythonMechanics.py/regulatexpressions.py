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

text = 'Мій номер 0991234567'
result = re.search(r'\d+', text)
print(result.group())  # '0991234567'




