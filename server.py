
from pysocket import PySocketServer

host = "192.168.219.106"
port = 8080

ps = PySocketServer(host, port)

def connect(client) :
    print(client.id, " connect!")

    client.emit("encrypt", "")

def disconnect(client) :
    print(client.id, " disconnect!")

def table(client) :
    print(client.id + " : " + client.data)

ps.on("connect", connect)
ps.on("disconnect", disconnect)
ps.on("table", table)

ps.connect()