import random as rand
import colorama as c
c.init(autoreset=True)
def choise(urinish,chos: str):
    lst = ['ong','chap','orta','ong tepa','chap tepa','past','tepa']
    plus = 0
    minus = 0
    while urinish > 0:
        a = input("Top tepmoqchi bolgan tarafingizni tanlang: ")
        if a in lst:
            if chos == 'easy':
                for i in range(2):
                    x = rand.choice(lst)
                    if x == a:
                        break
            elif chos == 'normal':
                for i in range(4):
                    x = rand.choice(lst)
                    if x == a:
                        break
            elif chos == 'hard':
                for i in range(5):
                    x = rand.choice(lst)
                    if x == a:
                        break

            if x == a:
                print()
                print(f"{c.Fore.RED}Afsuski siz gol ura olmadingiz.Siz {c.Fore.GREEN}{a}{c.Fore.RED} tarafga qarap tepdingiz va daravozabon ham shu tarafaga qarap sakradi.")
                minus += 1
            else:
                print()
                print(f"{c.Fore.YELLOW}Tabriklayman, siz gol urdingiz.{c.Fore.RESET}Siz{c.Fore.GREEN} {a} {c.Fore.YELLOW}tarafga qarap tepdingiz va darvozabon esa {c.Fore.RED}{x} tarafga qarap sakradi.")
                plus += 1
            print("Sizning hisobingiz.")
            print(f"{c.Fore.GREEN}{plus} : {c.Fore.RED}{minus}")
            urinish -= 1
        else:
            print("Siz no tugri tomonni kursatyapsiz.")
    if plus < minus:
        print(f"{c.Fore.RED} Oldin tepishni organip kelda pinalti seriyada ishtirok et iplos, shuncha vaqtni oldingda faqat.")
    elif plus == minus:
        print(f"{c.Fore.YELLOW}Bu oyin durrang natina bilan tugadi.Sizga ham katta rahmat.")
    else:
        print(f"{c.Fore.GREEN}Tabriklayman siz pinaltilar seriasida yutdingiz. Siz katta rahmat.")