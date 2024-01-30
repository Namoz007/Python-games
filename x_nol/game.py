import colorama as c 
import random as rand
c.init(autoreset=True)
def game():
    print("X va O o'yiniga xush kelibsiz.")
    game_end = 0
    while True:
        if game_end != 0:
            sur = input("Yana o'ynashni xoxlaysizmi.")
            if sur.lower() == 'yuq':
                print("Sizga katta rahmat.")
                break
            else:
                game_end = 0
        print("O'zingizga qaysi birinchi tanlaysiz.  X   yoki    0");count = 0
        you = input(">>>> ")
        if you.lower() == 'x':
            user = f"{c.Fore.GREEN}X{c.Fore.RESET}"
            komp = f"{c.Fore.RED}O{c.Fore.RESET}"
            count += 1
        elif you == '0':
            user = f"{c.Fore.GREEN}O{c.Fore.RESET}"
            komp = f"{c.Fore.RED}X{c.Fore.RESET}"
            count += 1
        else:
            print("Siz no to'g'ri ma'lumot kiritdingiz.")

        if count > 0:
            dct = {
                1 : '1',
                2 : '2',
                3 : '3',
                4 : '4',
                5 : '5',
                6 : '6',
                7 : '7',
                8 : '8',
                9 : '9'
            }
            lst = [1,2,3,4,5,6,7,8,9]
            while True:
                print(f"""
    {dct[1]} - {dct[2]} - {dct[3]}
    | \ | / |
    {dct[4]} - {dct[5]} - {dct[6]}
    | / | \ |
    {dct[7]} - {dct[8]} - {dct[9]}
""")
                if dct[1] == user and dct[2] == user and dct[3] == user:
                    print(f"Tabriklayman siz uchta {user}ni ketma ket joylashtirdingiz.")
                    game_end += 1
                    break
                elif dct[1] == user and dct[4] == user and dct[7] == user:
                    print(f"Tabriklayman siz uchta {user}ni ketma ket joylashtirdingiz.")
                    game_end += 1
                    break
                elif dct[4] == user and dct[5] == user and dct[6] == user:
                    print(f"Tabriklayman siz uchta {user}ni ketma ket joylashtirdingiz.")
                    game_end += 1
                    break
                elif dct[7] == user and dct[8] == user and dct[9] == user:
                    print(f"Tabriklayman siz uchta {user}ni ketma ket joylashtirdingiz.")
                    game_end += 1
                    break
                elif dct[2] == user and dct[5] == user and dct[8] == user:
                    print(f"Tabriklayman siz uchta {user}ni ketma ket joylashtirdingiz.")
                    game_end += 1
                    break
                elif dct[3] == user and dct[6] == user and dct[9] == user:
                    print(f"Tabriklayman siz uchta {user}ni ketma ket joylashtirdingiz.")
                    game_end += 1
                    break
                elif dct[1] == user and dct[5] == user and dct[9] == user:
                    print(f"Tabriklayman siz uchta {user}ni ketma ket joylashtirdingiz.")
                    game_end += 1
                    break
                elif dct[7] == user and dct[5] == user and dct[3] == user:
                    print(f"Tabriklayman siz uchta {user}ni ketma ket joylashtirdingiz.")
                    game_end += 1
                    break
                elif dct[4] == user and dct[5] == user and dct[6] == user:
                    print(f"Tabriklayman siz uchta {user}ni ketma ket joylashtirdingiz.")
                    game_end += 1
                    break
                elif dct[1] == user and dct[5] == user and dct[9] == user:
                    print(f"Tabriklayman siz uchta {user}ni ketma ket joylashtirdingiz.")
                    game_end += 1
                    break
                

                if dct[1] == komp and dct[2] == komp and dct[3] == komp:
                    print(f"Uchta {komp} ketma-ket joylashtirildi. Siz yutqazdingiz.")
                    game_end += 1
                    break
                elif dct[1] == komp and dct[4] == komp and dct[7] == komp:
                    print(f"Uchta {komp} ketma-ket joylashtirildi. Siz yutqazdingiz.")
                    game_end += 1
                    break
                elif dct[4] == komp and dct[5] == komp and dct[6] == komp:
                    print(f"Uchta {komp} ketma-ket joylashtirildi. Siz yutqazdingiz.")
                    game_end += 1
                    break
                elif dct[7] == komp and dct[8] == komp and dct[9] == komp:
                    print(f"Uchta {komp} ketma-ket joylashtirildi. Siz yutqazdingiz.")
                    game_end += 1
                    break
                elif dct[2] == komp and dct[5] == komp and dct[8] == komp:
                    print(f"Uchta {komp} ketma-ket joylashtirildi. Siz yutqazdingiz.")
                    game_end += 1
                    break
                elif dct[3] == komp and dct[6] == komp and dct[9] == komp:
                    print(f"Uchta {komp} ketma-ket joylashtirildi. Siz yutqazdingiz.")
                    game_end += 1
                    break
                elif dct[1] == komp and dct[5] == komp and dct[9] == komp:
                    print(f"Uchta {komp} ketma-ket joylashtirildi. Siz yutqazdingiz.")
                    game_end += 1
                    break
                elif dct[7] == komp and dct[5] == komp and dct[3] == komp:
                    print(f"Uchta {komp} ketma-ket joylashtirildi. Siz yutqazdingiz.")
                    game_end += 1
                    break
                elif dct[4] == komp and dct[5] == komp and dct[6] == komp:
                    print(f"Uchta {komp} ketma-ket joylashtirildi. Siz yutqazdingiz.")
                    game_end += 1
                    break
                elif dct[1] == komp and dct[5] == komp and dct[9] == komp:
                    print(f"Uchta {komp} ketma-ket joylashtirildi. Siz yutqazdingiz.")
                    game_end += 1
                    break

                choise = int(input(f"Siz qaysi raqam o'rniga {user}ni yozmoqchisiz: "));chois_count = 0
                if choise < 10:
                    if dct[choise] == str(choise):
                        dct[choise] = user
                        chois_count += 1
                    else:
                        print(f'Bu yerga siz {user}ni qoya olmaysiz.')
                else:
                    print("Bunaqa o'rin mavjud emas.")
                
                if chois_count > 0:
                    while True:
                        ran = int(rand.choice(lst))
                        # if dct[ran] != user and dct[ran] != komp:
                        if dct[ran] != user:
                            if dct[ran] != komp:
                                dct[ran] = komp
                                break
