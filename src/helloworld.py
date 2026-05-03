
# def sayword():
#     while True:
#         try:
#             word = input('Enter your word: ')
#             if word.isdigit():
#                 print("це число")
#             else:
#                 print(word + ' word')
#         except Exception:
#             print('Something went wrong')
        
#         # ✅ просто після try/except, без finally
#         answer = input('Do you want one more game? (yes/no): ')
#         if answer.lower() != 'yes':
#             print('Goodbye!')
#             break

# sayword()

def kakulator():
    while True:
        number1 = input('Your first number: ')
        number2 = input('Your second number: ')
        
        if not number1.isdigit() or not number2.isdigit():  # ✅ перевіряємо обидва
            print('Це не число!')
            break
        else:
            number1 = int(number1)
            number2 = int(number2)
            print('Числа прийнято!')
        print('chose ypur action')
        print('1 - додавання')
        print('2 - віднімання')
        print('3 - множення')
        print('4 - ділення')

        action = input('Your choice: ')
        if action == "1":
            print(number1 + number2)
        elif action == "2":
            print(number1 - number2)
        elif action == "3":
            print(number1 * number2)
        elif action == "4":
            print(number1 / number2)
        else :
            print('we dont have this option')
        
        answer = input("do you want start new game:")
        if answer.lower() == 'no' :
            print('Goodbye') 
            break
kakulator()