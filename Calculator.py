# Калькуоятор +-*/


from colorama import init
from colorama import Fore, Back, Style
init()
print(Fore.RED)
print( Back.BLACK)
what = input('что делаем (+, -):')




a = float(input('Enter 1 st number'))
b = float(input('Enter 2nd number'))
if what == "+":
     c = a + b
     print('result:' + str(c))
elif what == '-':
    c = a - b
    print('result:' + str(c))
else:
    print('You pick the wrong operation!')



