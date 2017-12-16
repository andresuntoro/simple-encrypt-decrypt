import binascii, sys
# Andre Suntoro - 201581076

def main():
	print "==================================="
	print "Penyisipan"
	print "==================================="
	print "1. Encryption"
	print "2. Decryption"
	print "3. Quit"

def enc():
	plain_teks=raw_input('Masukan Plaintext: ')
	plain=bin(int(binascii.hexlify(plain_teks), 16))
	i=2
	plainbin=[]
	while i!=len(plain):
		plainbin.append(plain[i])
		i=i+1
	plain=''.join(plainbin)
	print ("Binary Plainteks: "), plain

	key_teks=raw_input('Masukan Key: ')
	key=bin(int(binascii.hexlify(key_teks), 16))
	i=2
	keybin=[]
	while i!=len(key):
		keybin.append(key[i])
		i=i+1
	key=''.join(keybin)
	print ("Binary Key: "), key

	a = int(plain,2) ^ int(key,2)
	done = bin(a)[2:].zfill(len(plain))
	print "===================[HASIL]================="
	print ("Binary Chiperteks: "), done
	print "==========================================="

def dec():
	cipher_teks=raw_input('Masukan Binary dari Chiperteks:\n>>> ')
	key_teks=raw_input('Masukan Key: ')
	key=bin(int(binascii.hexlify(key_teks), 16))
	i=2
	keybin=[]
	while i!=len(key):
		keybin.append(key[i])
		i=i+1
	key=''.join(keybin)
	b = int(cipher_teks,2) ^ int(key,2)
	done = bin(b)[2:].zfill(len(cipher_teks))
	print "===================[HASIL]================="
	print ("Binary Plainteks: "), done
	print "==========================================="


if __name__ == '__main__':
	main()
	pilih = input("Masukan Pilihan: ")
	if pilih == 1:
		enc()
	elif pilih == 2:
		dec()
	elif pilih == 3:
		quit()
