import getpass
import string

authorized_users = {
				'root': 'root123.',
				'John': 'John123.',
				'Michael': 'Michael123.',
				'Alice': 'Alice123.',
				'Raichel': 'Raichel123.'
				}
while True:
	try:
		name = input('Please enter your name: ')
		if name == '':
			raise RuntimeError
		print('Hello, {}'.format(name))
		password  = getpass.getpass('Please enter your password: ')
		if authorized_users[name] == password:
			print('Access Granted!')
			break
	except KeyError:
		print("There's no such user registered!")
	except RuntimeError:
		print('Empty names are considered as a breach try!')
		
for symbol in authorized_users[name]:
	if symbol in string.punctuation:
		new_password = getpass.getpass('Your password has unacceptable symbol in it: {} Please change your password: '.format(symbol))
		authorized_users[name] = new_password
		print('Your password is successfully updated!')
		
	
		

		
		
		
