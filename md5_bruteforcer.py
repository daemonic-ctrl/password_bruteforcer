import password_hasher

def find_hash(file_name, op):
	# open file and checks to see if 'op' is in the file then returns the line it is on
	# used to display message if no hash is found
	found = False

	print('\n===========================================')
	print('[*] Opening File...')

	try:
		with open(file_name) as file_content:
			contents = file_content.readlines()

		print('[*] Starting Hash Search...')
		for content in contents:
			if op in content:
				print('[*] Hash Found!')
				print('===========================================\n')
				print('{}\n'.format(content.strip()))
				found = True

		if found == False:
			print('[*] Hash Not Found')

	except:
		print('[!] Error')
		print('[*] Check file name and try again.')


cont = True

print('\n---HashBack v1.0---\n')
print('Do you want to format and hash an existing text file or search a formated file for a hash?')

while cont == True:
	choice = str(input('\nformat or search: '))

	if choice in ('search','saerch','s'):
		file_name = str(input('\nEnter File to Search: '))
		hash = str(input('Enter Hash: '))
		find_hash(file_name, hash)

	elif choice in ('format', 'formate', 'f'):
		input_file = str(input('\nEnter File to Format: '))
		output_file = str(input('Enter Output File name: '))
		print('===========================================\n')
		password_hasher.check_exists(input_file, output_file)

	elif choice in ('Quit', 'stop', 'quit', 'exit', 'q'):
		cont = False

	else:
		print('[!] Sorry Answer was Not Understood Try Again')

	# allows for the ability to do multiple operations without restarting program
	again = str(input('Do you want to preform further actions? (yes or no): '))

	if again in ('no', 'n', 'No'):
		cont = False
	if again in ('yes', 'y', 'Yes'):
		print('\n\n')

print('\nThank You for using HashBack v1.0...Goodbye :)')
