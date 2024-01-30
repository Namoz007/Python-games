import colorama as c
import new_funk2 as nw
c.init(autoreset=True)
while True:
    on_tepa = "ong tepa"
    chap_tepa = 'chap tepa'
    on = "ong"
    chap = 'chap'
    past_taraf = 'past'
    orta = "orta"
    tepa = 'tepa'
    print("Salom.Xush kelibsiz bizni fashipka FIFA uyinimizga.Siz bu yerda penalti tepasiz.")
    print("Siz oz qiyinchilik darajangizi tanlang: ")
    while True:
        chos = input(f"{c.Fore.GREEN}easy   --    {c.Fore.YELLOW}normal   --  {c.Fore.RED}hard --> {c.Fore.RESET}")
        if chos == 'easy' or chos == 'normal' or chos == 'hard':
            break
        else:
            print("Siz no tugri qiyinchilik kiritdingiz.")
    
    while True:
        urinish = int(input("Siz jami nechta top tepmoqchisiz: --> Max - 15 and Min 3 --> "))
        if int(urinish) > 2 and urinish < 16:
            break
        elif urinish > 15:
            print("Siz juda ham kop urinish kiritdingiz.")
        elif urinish < 3:
            print('Siz juda ham kam urinish kiritdingiz.')
    print(f'''
        ______________________________________________________                             
        |                        {c.Fore.RED}{tepa}                        |                                                                   
        |                        ______                      |     
        |   {c.Fore.GREEN}{on_tepa}            / ~  ~ \      {c.Fore.YELLOW}{chap_tepa}      |
        |                      |   ~    |                    |
        |                       \  ~~  /                     |
        |                   _ _ |    |_ _                    | 
        |                   / |        |  \                  |             
        |                  / /|        |\ \                  |
        |                 / / |        | \ \                 |
        |     {c.Fore.WHITE}{on}        /_/  |        |  \_\       {c.Fore.BLUE}{chap}     |
        |               /     |  ___   \      \              |
        |                     /  /   \  \                    |
        |                    / /       \ \                   |
        |                   |  |       |  |                  |
        |                   |  |       |  | 
                            |  |  {c.Fore.GREEN}{past_taraf} |  |
                            ----       ----
    ''')            
    
    nw.choise(urinish,chos)

    y = input("RESTART or END --> ")
    if y == 'END':
        break