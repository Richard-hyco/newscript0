print "Halo Selamat Datang di Test Ini"
time.sleep(1)
jalan("\033[1;97mSelamat datang \033[1;92mSiapa Nama Kamu?\n\033[1;97mTerimakasih telah menggunakan tools ini !!")
		time.sleep(1)
        nama = raw_input("\033[1;97mSiapa nama kamu ? \033[1;91m: \033[1;92m")
	if nama =="":
  print"\033[1;96m[!] \033[1;91mIsi yang benar"
		time.sleep(1)
		siapa()
	else:
		os.system('clear')
		jalan("\033[1;97mSelamat datang \033[1;92m" +nama+ "\n\033[1;97mTerimakasih telah menggunakan tools ini !!")
		time.sleep(1)
     os.system('clear')
     print"\033[1;97mLogin Dulu Dong\n"
	username = raw_input("\033[1;96m[*] \033[1;97mUsername \033[1;91m: \033[1;92m")
	password = raw_input("\033[1;96m[*] \033[1;97mPassword \033[1;91m: \033[1;92m")
	if username =="Python" and password =="Test":
		print"\033[1;96m[✓] \033[1;92mLogin success"
		time.sleep(1)
		login()
	else:
		print"\033[1;96m[!] \033[1;91mSalah!!"
		time.sleep(1)
