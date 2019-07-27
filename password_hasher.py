import hashlib, os

def hasher(word):
	# turns strings into the MD5 hash of it's self
	hass = hashlib.md5(word.encode())
	return hass.hexdigest()


def outputting(input_file, hash_file, output_file):
	# passes contents of input_file to 'hasher()' function then outputs results to output_file
	print('[*] Opening Input File')
	with open(input_file) as wordlist:
		contents = wordlist.readlines()
		print('[*] Hashing and Formating Input File')
		for content in contents:
			word_hash = hasher(content.strip())
			hash_file.write('{0} = {1}\n'.format(word_hash, content))
		print('[*] Hashing Complete')
		print('[*] Outputing to {}\n'.format(output_file))
		print('===========================================\n')

def check_exists(input_file, output_file):
	# checks to see if Output_file exists, if not then it creates and opens it
	# then it runs the outputting_tup() function passing the input_file and
	# the now open and renamed hash_file (IE. the output_file)
	test = False
	while test == False:
		try:
			print('[*] Opening Output File')
			with open(output_file, 'w') as hash_file:
				test = True
				outputting(input_file, hash_file, output_file)
		except:
			print('[*] Output File Not Found')
			print('[*] Creating Output File')
			os.system('touch {}'.format(output_file))
			print('[*] Output File Created')
