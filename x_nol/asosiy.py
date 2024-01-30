import login as log
import registration as reg
import game as game
import colorama as c 
import random as rand
c.init(autoreset=True)
belgi = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=','/','?',"\\",'|','`','~',';',',']
belgi1 = ['@','$','^','&','_']
raqam = str('1234567890')
print(f"{c.Fore.GREEN}X va O oyinimzga xush kelibsiz.")
while True:
    enter = input(f"{c.Fore.RED}Login         -->\n{c.Fore.BLUE}Registration  -->{c.Fore.RESET}\n>>>> ")
    if enter.lower() == 'login':
        send = True
        if log.login(send):
            game.game()
    elif enter == 'Registration' or enter == 'registration':
        reg.registration()
    else:
        print(f"{c.Fore.RED}Siz no to'g'ri buyruq berdingiz.")
