from random import randint
from time import sleep
import os
from pathlib import Path
from colorama import Fore
from colorama import init as colorama_init

colorama_init(autoreset=True)


class User:

    def __init__(self):
        self.cwd = Path(__file__).parent
        self.usernames_txt = os.path.join(self.cwd, "usernames.txt")
        self.cwd2 = Path(__file__).parent
        self.passwords_txt = os.path.join(self.cwd2, "passwords.txt")
        self.cwd3 = Path(__file__).parent
        self.current_user_txt = os.path.join(self.cwd3, "current_user.txt")
        self.cwd4 = Path(__file__).parent
        self.users = os.path.join(self.cwd4, "users\\")

    def sign_up(self):
        characters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                      'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b',
                      'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                      'v', 'w', 'x', 'y', 'z', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '{', '[', ']', '}',
                      '\\', ' ', '?', '/', '>', '.', '<', ',', '"', "'", '+', '-', '-', '=', '`', '~', ';', ':']
        user = ''
        password = ''
        userfort = False
        ul = []
        file = open(self.usernames_txt, 'r')
        if not file == '':
            ul = file.read().split('|')
        file.close()
        print(Fore.RED + "************************************")
        print(Fore.RED + "************************************")
        print(Fore.RED + "************************************")
        print(Fore.RED + "      FOR MAKING ACCOUNT USE        ")
        print(Fore.RED + "   WORDS AND NUMBERS FOR USERNAME   ")
        print(Fore.RED + "               !!!!                 ")
        print(Fore.RED + "************************************")
        print(Fore.RED + "************************************")
        print(Fore.RED + "************************************")
        while userfort == False:
            numbering = 0
            user = str(input('\n\n\n\n\nUSERNAME : '))
            for x in range(len(ul)):
                if user == ul[x]:
                    numbering += 0
                elif user != ul[x]:
                    numbering += 1
            if numbering == len(ul):
                userfort = True
            else:
                print(Fore.RED + 'Error : the user exist')
                userfort = False
        with open(self.usernames_txt, 'a') as fileu:
            fileu.write(user + "|")
        passtype = str(input('Do want to enter your password by hand or by bot (hand/bot) : '))
        if passtype.lower() == 'bot':
            length = int(input("how many characters it should be ? "))
            for x in range(length):
                password += characters[randint(0, (len(characters) - 1))]
                if x + 1 == length:
                    print('\n\n')
                    print(Fore.YELLOW + "This is your password : ", password)
        else:
            password = str(input("Password : "))
        with open(self.passwords_txt, 'a') as filep:
            filep.write(password + '|')
        f = open(self.users + user + '.txt', 'x')
        f.close()
        print('\n\n')
        print(Fore.GREEN + 'account made succesfully!')
        with open(self.current_user_txt, 'w') as current:
            current.write(user)
        return True

    def login(self):
        torfu = 0
        torfp = 0
        # gottenUsername = ''
        # gottenpassword = ''
        userindex = 0
        with open(self.usernames_txt, 'r') as u:
            usernames = u.read().split('|')
        with open(self.passwords_txt, 'r') as p:
            passwords = p.read().split('|')
        while torfu != 1:
            gottenUsername = str(input('Enter your username : '))
            for x in range(len(usernames)):
                if gottenUsername == usernames[x]:
                    userindex += x
                    torfu += 1
                    break
        while torfp != 1:
            gottenpassword = str(input('Enter your password : '))
            if gottenpassword == passwords[userindex]:
                print('\n\n')
                print(Fore.GREEN + 'You loged in succesfully!')
                torfp = 1
            else:
                print(Fore.RED + 'Password is wrong!')
                torfp = 0
        with open(self.current_user_txt, 'w') as current:
            current.write(gottenUsername)
        return True, gottenUsername, gottenpassword

    def add_note(self):
        username = ''
        with open(self.current_user_txt, 'r') as bb:
            username += bb.read()
        note = str(input("Enter your note : " + '\n'))
        with open(self.users + username + '.txt', 'a') as noteFile:
            noteFile.write('\n' + note)
        self.show_options()

    def show_note(self):
        username = ''
        with open(self.current_user_txt, 'r') as cc:
            username += cc.read()
        print('\n\nYour Notes :\n')
        with open(self.users + username + '.txt', 'r') as readedlines:
            print(readedlines.read())
        self.show_options()

    def rewrite_note(self):
        username = ''
        with open(self.current_user_txt, 'r') as dd:
            username += dd.read()
        note = str(input("Enter your note : " + '\n'))
        with open(self.users + username + '.txt', 'w') as noteFile:
            noteFile.write(note)
        self.show_options()

    def log_out(self):
        with open(self.current_user_txt, 'w') as ee:
            ee.write('')
        print(Fore.BLUE + 'loging out...')
        sleep(5)
        exit()

    def show_options(self):
        sleep(3)
        print('\n\n\n')
        print('             OPTIONS    \n')
        print('1. show note')
        print('2. add notes')
        print('3. rewrite note')
        print('4. log out')
        print('\n             !!!PLEASE CHOOSE ONE NUMBER OF LIST!!!')
        choose = str(input(''))
        while True:
            if choose == '1':
                self.show_note()
                break
            elif choose == '2':
                self.add_note()
                break
            elif choose == '3':
                self.rewrite_note()
                break
            elif choose == '4':
                self.log_out()
                break

            else:
                print(Fore.RED + 'Error:this is not one number of the list')
