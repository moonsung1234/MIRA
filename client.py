
import os
import requests
from pysocket import PySocketClient
from rsa import decrypt
from crypto import Crypto

ip = requests.get("http://ip.jsontest.com").json()["ip"]
host = "192.168.219.106" if ip == "125.182.224.34" else "http://m.moonsung.o-r.kr"
port = 8080

print(host)

ps = PySocketClient(host, port)
ct = Crypto()

def encrypt(server) :
    result, table = ct.encrypt_file("test.txt")

    server.emit("table", str(table))
    # result = ct.decrypt_file("test.txt", table)

def decrypt(server) :
    table = server.data[1:-1].split(",")

    for i in range(len(table)) :
        table[i] = int(table[i])

    result = ct.decrypt_file("test.txt", table)

ps.on("encrypt", encrypt)
ps.on("decrypt", decrypt)

ps.connect()