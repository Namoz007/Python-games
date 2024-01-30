import colorama as c 
c.init(autoreset=True)
belgi = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=','/','?',"\\",'|','`','~',';',',']
belgi1 = ['@','$','^','&','_']
raqam = str('1234567890')
end = 0
def registration():
        end = 0
        while True:
            registration_name = input("Iltimos ismingizni kiriting: ");log_true = 0
            if registration_name.lower() == 'exit':
                end += 1
                break
            for i in registration_name:
                if i in belgi:
                    print(f"{c.Fore.RED}Ismda belgi bo'lmasligi kerak.{c.Fore.RESET}")
                    break
                elif i in raqam:
                    print(f"{c.Fore.RED}Ismda raqam bo'lmasligi kerak.{c.Fore.RESET}")
                    break
                else:
                    log_true += 1
            login_kirish = 0
            if log_true == len(registration_name):
                with open("x_nol/loginlar.txt") as f:
                    for i in f.read().split("\n"):
                        j = i.split(":")[0]
                        if j == registration_name:
                            print("Bunaqa login mavjud iltimos boshqa login kiriting.")
                            login_kirish = 0
                            break
                        else:
                            login_kirish += 1
            if login_kirish > 0:
                while True:
                    print("Parolda kamida 1 ta: katta harf,kichik harf,raqam,belgi va kamida 8 ta element bo'lishi shart.");shart = 0
                    login_password = input("Parolni kiriting: "); par_count = 0
                    while True:
                        if login_password[0] in belgi:
                            print(f"{c.Fore.RED}Parolni birinchi elementi belgi bo'lishi mumkin emas.{c.Fore.RESET}")
                            break
                        elif login_password[0] in raqam:
                            print(f"{c.Fore.RED}Parolni birinchisi raqam bo'lishi mukin emas.{c.Fore.RESET}")
                            break
                        else:
                            par_count += 1
                        par_raqam = 0; par_belg = 0; par_kaharf = 0; par_kiharf = 0
                        if par_count == len(login_password):
                            for i in login_password:
                                if i in belgi1:
                                    par_belg += 1
                                elif i in belgi:
                                    print(f"{c.Fore.RED}{i} Bunaqa belgidan foydalanish mumkin emas.{c.Fore.RESET}")
                                    shart += 1
                                    break
                                elif i in raqam:
                                    par_raqam += 1
                                elif i.islower():
                                    par_kiharf += 1
                                elif i.isupper():
                                    par_kaharf += 1
                            if shart == 0:
                                if len(login_password) >= 8:
                                    if par_raqam > 0:
                                        if par_belg > 0:
                                            if par_kaharf > 0:
                                                if par_kiharf > 0:
                                                    with open('x_nol/loginlar.txt','a') as f:
                                                        f.write(registration_name)
                                                        f.write(":")
                                                        f.write(login_password)
                                                        f.write("\n")
                                                        print("Siz muvafaqqiyatli ro'yxatdan o'tdingiz.")
                                                        end += 1
                                                        shart += 1
                                                else:
                                                    print(f"{c.Fore.RED}Siz kiritgan parolda kichik harf mavjud emas.{c.Fore.RESET}")
                                                    shart += 1
                                            else:
                                                print(f"{c.Fore.RED}Siz kiritgan prol katta harf mavjud emas.{c.Fore.RESET}")
                                                shart += 1
                                        else:
                                            print(f"{c.Fore.RED}Siz kiritgan parolda belgi mavjud emas.{c.Fore.RESET}")
                                            shart += 1
                                    else:
                                        print(f"{c.Fore.RED}Siz kiritgan parolda raqam mavjud emas.{c.Fore.RESET}")
                                        shart += 1
                                else: 
                                    print(f"{c.Fore.RED}Parol kamida 8 ta elementdan iborat bo'lishi kerak.{c.Fore.RESET}")
                                    shart += 1
                            if shart > 0:
                                break
                        if shart > 0:
                            break
                    if end > 0: 
                        break
            if end > 0:
                break