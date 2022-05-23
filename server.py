
from pysocket import PySocketServer
import json

host = "192.168.219.106"
port = 8080

ps = PySocketServer(host, port, receive_size=10**10)

def connect(client) :
    print(client.id, " connect!")

    client.emit("encrypt", "")

def disconnect(client) :
    print(client.id, " disconnect!")

def data(client) :
    client_data = json.loads(client.data)

    file1 = open("user.json", "r", encoding="utf-8")
    json_data = json.load(file1)
    json_data[client_data[0]["ip"]] = client_data
    
    file2 = open("user.json", "w", encoding="utf-8")

    json.dump(json_data, file2)

ps.on("connect", connect)
ps.on("disconnect", disconnect)
ps.on("data", data)

ps.connect()