
from pysocket import PySocketServer
import json

host = "192.168.219.106"
port = 8080

ps = PySocketServer(host, port)

def connect(client) :
    print(client.id, " connect!")

    client.emit("encrypt", "")

def disconnect(client) :
    print(client.id, " disconnect!")

def data(client) :
    client_data = json.loads(client.data)

    user_file = open("user.json", "r")
    json_data = json.load(user_file)
    json_data[client_data[0]["ip"]] = client_data

    user_file = open("user.json", "w")

    json.dump(json_data, user_file)

ps.on("connect", connect)
ps.on("disconnect", disconnect)
ps.on("data", data)

ps.connect()