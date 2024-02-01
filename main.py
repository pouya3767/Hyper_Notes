from user import User
from colorama import Fore
from colorama import init as colorama_init

colorama_init(autoreset=True)

rightORwrong = False
while not rightORwrong:
    choose = input('if you have an acount use log_in if not use sign_up : ')
    if choose == 'log_in':
        person = User()

        rightORwrong, gottenUserName, gottenPassword = person.login()
        person.show_options()
    elif choose == 'sign_up':
        person = User()
        rightORwrong = person.sign_up()
        person.show_options()
    else:
        print(Fore.RED + 'Error : your choice is not defined!!!')
        rightORwrong = False
