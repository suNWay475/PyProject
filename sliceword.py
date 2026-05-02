from collections import deque
def sliceword():
    words = input('Enter your word: ')
    letters = deque(words)   # deque сам розкладає рядок по символах
    for word in words :
        print(word)

sliceword()
