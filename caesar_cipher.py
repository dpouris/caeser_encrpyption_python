#Caesar Cipher Python Encrypter

import string
import collections

def caesar_cipher(message, rot):
	upper = collections.deque(string.ascii_uppercase)
	lower = collections.deque(string.ascii_lowercase)

	upper.rotate(rot)
	lower.rotate(rot)

	upper = ''.join(upper)
	lower = ''.join(lower)

	upper_trans_table = message.maketrans(string.ascii_uppercase,upper)
	lower_trans_table = message.maketrans(string.ascii_lowercase,lower)

	cihpered_message = message.translate(upper_trans_table).translate(lower_trans_table)

	return cihpered_message,rot

def un_caesar_cipher():
	message = input('\nWrite your encrypted message here: ')
	rot = int(input('Input your encryption number: '))
	un_rot = 26 - rot
	upper = collections.deque(string.ascii_uppercase)
	lower = collections.deque(string.ascii_lowercase)

	upper.rotate(un_rot)
	lower.rotate(un_rot)

	upper = ''.join(upper)
	lower = ''.join(lower)

	upper_trans_table = message.maketrans(string.ascii_uppercase,upper)
	lower_trans_table = message.maketrans(string.ascii_lowercase,lower)

	un_ciphered_message = message.translate(upper_trans_table).translate(lower_trans_table)

	print(f'\n\nThis is your de-crypted message: {un_ciphered_message}\n')

while True:
	print('''       
░█████╗░░█████╗░███████╗░██████╗░█████╗░██████╗░  ░█████╗░██╗██████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗  ██╔══██╗██║██╔══██╗██║░░██║██╔════╝██╔══██╗
██║░░╚═╝███████║█████╗░░╚█████╗░███████║██████╔╝  ██║░░╚═╝██║██████╔╝███████║█████╗░░██████╔╝
██║░░██╗██╔══██║██╔══╝░░░╚═══██╗██╔══██║██╔══██╗  ██║░░██╗██║██╔═══╝░██╔══██║██╔══╝░░██╔══██╗
╚█████╔╝██║░░██║███████╗██████╔╝██║░░██║██║░░██║  ╚█████╔╝██║██║░░░░░██║░░██║███████╗██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝  ░╚════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
______________________________________________________________________________________________

				   1. E̷n̷c̷r̷y̷p̷t̷[]
				   2. D̲e̲-̲C̲r̲y̲p̲t̲{}
				   3. Exit()	
______________________________________________________________________________________________
					██████╗░██████╗░
					██╔══██╗██╔══██╗
					██║░░██║██████╔╝
					██║░░██║██╔═══╝░
					██████╔╝██║░░░░░
					╚═════╝░╚═╝░░░░░



		''')
	choose_function = int(input('Choose what you want to do: '))
	if choose_function == 1:

		message = input('\nWrite the message you want to encrypt!: ')
		rot = int(input('Type the number from 1-25 to determine the encryption type: '))

		ciphered_message,un_cipher_number = caesar_cipher(message,rot)

		print(f'\n\nYour encrypted message: {ciphered_message}')
		print(f'If you wish to de-crypt the message this is your code: {un_cipher_number}\n')
		pass
	elif choose_function == 2:
		un_caesar_cipher()
		pass
	else:
		exit()
	prompt = input('Do you wish to continue?(y/n): ')
	if prompt == 'y':
		print('\n'*100)
		pass
	else:
		exit()