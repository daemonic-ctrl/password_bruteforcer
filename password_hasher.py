import hashlib

def hasher(word):
	hass = hashlib.md5(word.encode())
	return hass.hexdigest()
fil = str(input('Enter file name: '))

wordlist = open(fil)
hash_file = open('hashes.txt', 'w')

print('[*] Hashing Started.')

for word in wordlist:

	word_hash = hasher(word)
	hash_file.write('{0},{1}\n'.format(word_hash, word))

hash_file.close()
wordlist.close()
print('[*] complete.')
