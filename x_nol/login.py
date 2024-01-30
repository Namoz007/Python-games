import colorama as c
c.init(autoreset=True)
belgi = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=','/','?',"\\",'|','`','~',';',',']
belgi1 = ['@','$','^','&','_']
raqam = str('1234567890')
def login(send: bool) -> bool:
    log_now = 0
    if send == True:
        while True:
            if log_now > 0:
                break
            while True:
                login_name = input("Ismingizni kiriting: "); log_count = 0; log_pass = str();log_you = 0
                if login_name.lower() == 'exit':
                    log_now += 1
                    break
                with open('x_nol/loginlar.txt') as f:
                    for i in f.read().split("\n"):
                        j = i.split(":")[0]
                        if login_name == j:
                            log_count += 1
                            log_pass = i.split(":")[1]
                            break
                    if log_count > 0:
                        log_you += 1
                        break
                    else:
                        print(f"{c.Fore.RED}Siz kiritgan login mavjud emas.{c.Fore.RESET}")
            while True:
                if log_you > 0:
                    login_password = input("Iltimos parolni kiriting: ")
                    if log_pass == login_password:
                        return True
                    elif login_password.lower() == 'exit':
                        break
                    else:
                        print("Siz kiritgan parol no to'g'ri.")
                else:
                    break
