import csv

port1 = 'PORTAL REGISTRASI'
port2 = 'PORTAL LOGIN'

#REGISTRASI
def registrasi():
	print(port1.center(50, '='))
	with open("username.csv", "a") as x:
		writer = csv.writer(x, delimiter=",")
		user = input('Username 		: ')
		passw = input('Password 		: ')
		ulang_passw = input('Ulangi password : ')
		if passw == ulang_passw:
			writer.writerow([user, passw])
			print('Silakan login dengan username dan password yang dibuat!\n')
		else:
			print("Password tidak sama! Silakan registrasi ulang!\n")
			registrasi()

#LOGIN
def login():
	print(port2.center(50, '='))
	user = input("Username : ")
	passw = input("Password : ")
	with open("username.csv", "r") as x:
		reader = csv.reader(x, delimiter=",")
		for row in reader:
			if row == [user, passw]:
				print("SUKSES")
				return True
	print("Username atau Password salah. Silakan coba lagi!\n")
	welcome()
	return False


#WELCOME
def welcome():
	print('MENU UTAMA'.center(50, '-'))
	print('Silakan registrasi atau login untuk akses')
	print('[1] Registrasi')
	print('[2] Login')
	menu = int(input('Masukkan pilihan Anda : '))

	if menu == 1:
		print('\n')
		registrasi()
		login()
	elif menu == 2:
		print('\n')
		login()
	else:
		print('Menu yang Anda masukkan salah!')

#Program
welcome()