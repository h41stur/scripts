#!/usr/bin/env python3

import sys
import string
import datetime
import re
import os
from unicodedata import normalize

dic = {'aioO':'@100','aeioOs':'43100$','aeiou':'AEIOU','IilLsS':'1111$$'}
wordlist = open(sys.argv[2]+'tmp', 'w')
data = datetime.datetime.now()
car = ['!','@','#','$','%','&','*','(',')','_','-','=','+','<','>',';',':','/','?','~','^','[','{',']','}']

def function_2 (word):
	for n in range(1001):
		wordlist.write(word+str(n)+'\n')
		wordlist.write(str(n)+word+'\n')
		for s in car:
			wordlist.write(word+str(s)+str(n)+'\n')
			wordlist.write(word+str(n)+str(s)+'\n')
			wordlist.write(str(s)+str(n)+word+'\n')
			wordlist.write(str(s)+word+str(n)+'\n')
			wordlist.write(str(n)+str(s)+word+'\n')
			wordlist.write(str(n)+word+str(s)+'\n')

def function_1 (line):
	for i in dic:
		wordlist.write(line.translate(str.maketrans(i,dic[i]))+'\n')
		function_2(line.translate(str.maketrans(i,dic[i])))
		wordlist.write(line.translate(str.maketrans(i,dic[i]))+str(data.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i])).upper()+'\n')
		function_2(line.translate(str.maketrans(i,dic[i])).upper())
		wordlist.write(line.translate(str.maketrans(i,dic[i])).upper()+str(data.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i])).lower()+'\n')
		function_2(line.translate(str.maketrans(i,dic[i])).lower())
		wordlist.write(line.translate(str.maketrans(i,dic[i])).lower()+str(data.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i])).capitalize()+'\n')
		function_2(line.translate(str.maketrans(i,dic[i])).capitalize())
		wordlist.write(line.translate(str.maketrans(i,dic[i])).capitalize()+str(data.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i])).title()+'\n')
		function_2(line.translate(str.maketrans(i,dic[i])).title())
		wordlist.write(line.translate(str.maketrans(i,dic[i])).title()+str(data.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i])).swapcase()+'\n')
		function_2(line.translate(str.maketrans(i,dic[i])).swapcase())
		wordlist.write(line.translate(str.maketrans(i,dic[i])).swapcase()+str(data.year)+'\n')

		for l in car:
			wordlist.write(line.translate(str.maketrans(i,dic[i]))+str(l)+str(data.year)+'\n')
			wordlist.write(line.translate(str.maketrans(i,dic[i])).upper()+str(l)+str(data.year)+'\n')
			wordlist.write(line.translate(str.maketrans(i,dic[i])).lower()+str(l)+str(data.year)+'\n')
			wordlist.write(line.translate(str.maketrans(i,dic[i])).capitalize()+str(l)+str(data.year)+'\n')
			wordlist.write(line.translate(str.maketrans(i,dic[i])).title()+str(l)+str(data.year)+'\n')
			wordlist.write(line.translate(str.maketrans(i,dic[i])).swapcase()+str(l)+str(data.year)+'\n')


def main():
	with open(sys.argv[1]) as file:
		for t in file:
			linha = t.rstrip('\n')
			function_1(linha)
	wordlist.close()

if __name__ == '__main__':
  main()

os.system("cat "+ sys.argv[2]+'tmp' + " | sort | uniq > " + sys.argv[2]+ '; rm ' + sys.argv[2]+'tmp')
